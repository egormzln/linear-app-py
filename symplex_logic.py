from array import ArrayType
from fractions import Fraction
from task_config import ExtremumType, SolutionType

class Result:
    def __init__(self):
        self.function_result = None
        self.basis_result = None
        self.comment = None

class SymplexLogic:
    def __init__(self):
        self.solution_type = None
        self.extremum_type = None
        # [ <массив шагов иск-го базиса>, <массив шагов симплекса>]
        self.steps = [[], []]
        self.result = Result()

    def gauss_method(self, matrix, target_columns):
        rows = len(matrix)
        num_columns = len(matrix[0])

        # Приведение диагонального элемента к 1 (нормировка)
        for row_index, col_index in enumerate(target_columns):
            # Элемент, который должен стать единичным
            pivot = matrix[row_index][col_index]

            # Делим все оставшиеся элементы строки, чтобы привести элемент к 1
            for j in range(num_columns):
                if pivot != Fraction(0):
                    matrix[row_index][j] /= pivot

            # Длаее для каждой строки (без pivot)
            for target_row in range(rows):
                if target_row != row_index:
                    factor = matrix[target_row][col_index]
                    for column in range(num_columns):
                        # Вычитаем factor кол-во строк pivot элемента, чтобы привести весь стобец под ним в единичную матрицу
                        matrix[target_row][column] -= factor * matrix[row_index][column]
        return matrix

    def reduce_function(self, function, gauss_matrix, basis, extremum_type):
        # Инициализируем новую функцию с нулевыми коэффициентами для базисных переменных
        new_function = []
        for i in range(len(function)):
            if basis[i] == 1:
                new_function.append(Fraction(0))
            else:
                new_function.append(function[i])
        # Добавляем свободный член (свободная переменная)
        new_function.append(Fraction(0))

        # Определяем индексы оставшихся переменных (не базисных)
        not_basis_indexes = []
        basis_indexes = []
        for i in range(len(basis)):
            if basis[i] != 1:
                not_basis_indexes.append(i)
            else:
                basis_indexes.append(i)

        # Проходим строкам метода Гаусса
        gauss_row_index = 0
        # Проходим по стобцам базисных переменных для вычисления свободнго коэфициента
        for basis_col_index in basis_indexes:
            delta = gauss_matrix[gauss_row_index][-1] * function[basis_col_index]
            new_function[-1] += delta
            gauss_row_index += 1

        for not_basis_col in not_basis_indexes:
            for gauss_row_index in range(len(gauss_matrix)):
                delta = gauss_matrix[gauss_row_index][not_basis_col] * function[basis_indexes[gauss_row_index]] * Fraction('-1')
                new_function[not_basis_col] += delta

        # Если нужно максимизировать функцию, меняем знаки всех коэффициентов
        # TODO(mzln) нужно это делать или нет
        # if extremum_type == ExtremumType.MAX:
        #     new_function = [-v for v in new_function]

        # Возвращаем уменьшенную функцию
        return new_function

    def get_initial_symplex_table(self, task_matrix, basis_vars, extremum_type):
        input_gauss_matrix = []
        basis = task_matrix[-1]
        for task_row in range(1, len(task_matrix) - 1):
            new_row = []
            for item in task_matrix[task_row]:
                new_row.append(item)
            input_gauss_matrix.append(new_row)

        gauss_result = self.gauss_method(input_gauss_matrix, basis_vars)

        reduced_function = self.reduce_function(task_matrix[0], gauss_result, basis, extremum_type)

        symplex_table = []

        # Определяем индексы оставшихся переменных (не базисных)
        not_basis_indexes = []
        basis_indexes = []
        for i in range(len(basis)):
            if basis[i] != 1:
                not_basis_indexes.append(i)
            else:
                basis_indexes.append(i)

        first_symplex_row = ['x(0)']
        for not_basis_index in not_basis_indexes:
            first_symplex_row.append(f'x{not_basis_index + 1}')

        symplex_table.append(first_symplex_row)

        gauss_row = 0
        for basis_index in basis_indexes:
            new_symplex_row = [f'x{basis_index + 1}']
            for not_basis_index in not_basis_indexes:
                new_symplex_row.append(gauss_result[gauss_row][not_basis_index])
            new_symplex_row.append(gauss_result[gauss_row][-1])
            gauss_row += 1
            symplex_table.append(new_symplex_row)

        final_symplex_row = ['f']
        for not_basis_index in not_basis_indexes:
                final_symplex_row.append(reduced_function[not_basis_index])
        final_symplex_row.append(reduced_function[-1] * -1)
        symplex_table.append(final_symplex_row)

        return symplex_table

    def get_available_support_elements(self, table):
        # {'Столбец': '<Значение>'}
        available_col_coeffs = {}
        for i in range(1, len(table[-1]) - 1):
            if table[-1][i] < 0:
                available_col_coeffs[i] = table[-1][i]

        # Сортиурем столбцы по минимальному значению
        sorted_available_col_coeffs = dict(sorted(available_col_coeffs.items(), key=lambda item: item[1]))

        available_support_elements = []
        for col_index in sorted_available_col_coeffs.keys():
            for row_index in range(1, len(table) - 1):
                if table[row_index][col_index] > 0:
                    new_support_element = table[row_index][col_index]
                    simplex_relation = table[row_index][-1] / table[row_index][col_index]
                    available_support_elements.append([new_support_element, simplex_relation, row_index, col_index])

        # Сортиурем эл-ты по симплексному отношению
        sorted_available_support_elements = sorted(available_support_elements, key=lambda x: x[1])

        return sorted_available_support_elements


    # [ Алгоритм симплекс метода ]
    # Возварщает новую симплекс таблицу, на основе старой.
    #
    # Пример работы:
    # while True
    #   new_step = self.symplex_step(steps[-1])
    #   steps.append(new_step)
    # print(steps)
    def symplex_step(self, old_symplex_table, selected_support_element=None, artificial_basis_method=False):
        old_st = old_symplex_table
        new_st = []

        # Делаем глубокую копию последней симплекс-таблицы
        for row in old_st:
            new_st_row = []
            for el in row:
                new_st_row.append(el)
            new_st.append(new_st_row)
            print(*new_st_row)
        print()

        # {'Столбец': '<Значение>'}
        available_col_coeffs = {}
        for i in range(1, len(new_st[-1]) - 1):
            if new_st[-1][i] < 0:
                available_col_coeffs[i] = new_st[-1][i]

        # Сортиурем столбцы по минимальному значению
        sorted_available_col_coeffs = dict(sorted(available_col_coeffs.items(), key=lambda item: item[1]))

        if len(sorted_available_col_coeffs) == 0:
            if artificial_basis_method:
                # TODO добавить проверку на все нули в строке оценок и реализовать алгоритм холостого шага
                print('Метод икусственного базиса завершён!')
                return old_st, True

            print('Нет доступных столбцов для выбора, симплекс-метод закончен!\n')

            result = new_st[-1][-1]
            if self.extremum_type == ExtremumType.MIN.name:
                result *= -1
            basis = self.generate_basis_output(new_st)

            return result, basis

        available_support_elements = []
        for col_index in sorted_available_col_coeffs.keys():
            for row_index in range(1, len(new_st) - 1):
                if new_st[row_index][col_index] > 0:
                    new_support_element = new_st[row_index][col_index]
                    simplex_relation = new_st[row_index][-1] / new_st[row_index][col_index]
                    available_support_elements.append([new_support_element, simplex_relation, row_index, col_index])

        sorted_available_support_elements = sorted(available_support_elements, key=lambda x: x[1])

        # Если опорных элементов нет
        if len(sorted_available_support_elements) == 0:
            print('Нет доступных строк для выбора, функция не ограничена снизу!')
            return None

        support_element = None

        if self.solution_type == SolutionType.AUTO:
            support_element = sorted_available_support_elements[0]
        elif self.solution_type == SolutionType.MANUAL and selected_support_element is not None:
            for el in sorted_available_support_elements:
                if selected_support_element == (el[-2], el[-1]):
                    support_element = el
                    break
            if support_element is None:
                support_element = sorted_available_support_elements[0]

        if support_element is None:
            return None

        print(f'Выбран элемент {str(support_element[0])} с отношением {str(support_element[1])} (столбец: {str(support_element[-1])}, строка: {str(support_element[-2])})\n')

        support_el_value = support_element[0]
        support_col_index = support_element[-1]
        support_row_index = support_element[-2]

        # Нулевой шаг симплекс метода
        # Xi -> Xi+1
        if artificial_basis_method:
            symplex_table_title = new_st[0][0].split('^')
            new_symplex_table_title = int(symplex_table_title[1]) + 1
            new_st[0][0] = f'x^{new_symplex_table_title}'
        else:
            symplex_table_title = [_ for _ in new_st[0][0]]
            left_bracket_index = symplex_table_title.index('(')
            right_bracket_index = symplex_table_title.index(')')
            symplex_table_title = [symplex_table_title[i] for i in range(left_bracket_index + 1, right_bracket_index)]
            new_symplex_table_title = ''
            for el in symplex_table_title:
                new_symplex_table_title += el
            new_symplex_table_title = int(new_symplex_table_title)
            new_st[0][0] = f'x({new_symplex_table_title + 1})'

        # Первый шаг симплекс метода
        # Xr <-> Xs
        buffer = new_st[support_row_index][0]
        new_st[support_row_index][0] = new_st[0][support_col_index]
        new_st[0][support_col_index] = buffer

        # Второй шаг симплекс метода
        # Asr^(1) = 1 / Ars^(0)
        new_st[support_row_index][support_col_index] = 1 / new_st[support_row_index][support_col_index]

        # Третий шаг симплекс метода
        # ROWs^(1) = 1 / Ars^(0) * ROWr^(0)
        for col_index in range(1, len(new_st[support_row_index])):
            if col_index != support_col_index:
                new_st[support_row_index][col_index] = 1 / support_el_value * old_st[support_row_index][col_index]

        # Четвёртый шаг симплекс метода
        # COLr^(1) = - 1 / Ars^(0) * COLs^(0)
        for row_index in range(1, len(new_st)):
            if row_index != support_row_index:
                new_st[row_index][support_col_index] = -1 / support_el_value * new_st[row_index][support_col_index]

        # Пятый шаг симплекс метода
        # i != s: ROWi^(1) = ROWi^(0) - Ais * ROWs^(1)
        for row_index in range(1, len(new_st)):
            for col_index in range(1, len(new_st[row_index])):
                if row_index != support_row_index and col_index != support_col_index:
                    new_st[row_index][col_index] = old_st[row_index][col_index] - old_st[row_index][support_col_index] * new_st[support_row_index][col_index]
                    # old = st[row_index][col_index]
                    # print(f'{old_st[row_index][col_index]} - {old_st[row_index][support_col_index]} * {new_st[support_row_index][col_index]}')
                    # print(f'{old} -> {new_st[row_index][col_index]}')
                    # input()

        if artificial_basis_method:
            # Доп. шаг метода искусственного базиса
            # Вырез столбца
            for row_index in range(len(new_st)):
                del new_st[row_index][support_col_index]

        return new_st

    def get_init_artificial_basis_table(self, task_matrix):
        # Добавляем шапку таблицы
        new_art = [['x^0']]
        new_var_num = len(task_matrix[0]) + 1
        for row_index in range(len(task_matrix[0])):
            new_art[0].append(f'x{row_index + 1}')

        # Добавляем строки с новыми переменными
        for row_index in range(1, len(task_matrix) - 1):
            new_art_row = [f'x{new_var_num}']
            for col_index in range(len(task_matrix[row_index])):
                new_art_row.append(task_matrix[row_index][col_index])
            new_art.append(new_art_row)
            new_var_num += 1

        # Добавляем строку оценок
        new_sum_row = ['f']
        for col_index in range(1, len(new_art[-1])):
            col_sum = 0
            for row_index in range(1, len(new_art)):
                col_sum += new_art[row_index][col_index]
            col_sum *= -1
            new_sum_row.append(col_sum)
        new_art.append(new_sum_row)

        return new_art

    def generate_basis_output(self, st):
        basis_arr = [Fraction(0)] * ((len(st) - 2) + (len(st[0]) - 1))
        for row_index in range(1, len(st) - 1):
            literals = [i for i in st[row_index][0]]
            var_index = ''
            for i in range(1, len(literals)):
                var_index += literals[i]
            basis_arr[int(var_index)-1] = st[row_index][-1]
        return basis_arr

    def get_basis_vars(self, task_matrix):
        basis_vars = []
        for i in range(len(task_matrix[-1])):
            if task_matrix[-1][i] == Fraction(1):
                basis_vars.append(i)
        return basis_vars

    def solve_task(self, task_matrix, extremum_type, solution_type):
        self.extremum_type = extremum_type
        self.solution_type = solution_type

        initial_symplex_table = None

        basis_vars = self.get_basis_vars(task_matrix)

        if len(basis_vars) == len(task_matrix) - 2:
            # input_gauss_matrix = []
            # for task_row in range(1, len(task_matrix) - 1):
            #     new_row = []
            #     for item in task_matrix[task_row]:
            #         new_row.append(item)
            #     input_gauss_matrix.append(new_row)
            #
            # gauss_result = self.gauss_method(input_gauss_matrix, basis_vars)
            #
            # reduced_function = self.reduce_function(task_matrix[0], gauss_result, task_matrix[-1], extremum_type)

            initial_symplex_table = self.get_initial_symplex_table(task_matrix, basis_vars, extremum_type)

            self.steps[1] = [initial_symplex_table]

            while True:
                symplex_result = self.symplex_step(self.steps[1][-1])
                if isinstance(symplex_result, list):
                    self.steps[1].append(symplex_result)
                elif isinstance(symplex_result, tuple):
                    self.result.function_result = symplex_result[0]
                    self.result.basis_result = symplex_result[1]
                    self.result.comment = "Задача успешно решена!"

                    return symplex_result
                elif symplex_result is None:
                    return symplex_result

        elif sum(task_matrix[-1]) == Fraction(0):
            print('Метод искуственного базиса!\n')
            initial_artificial_basis_table = self.get_init_artificial_basis_table(task_matrix)

            self.steps[0] = [initial_artificial_basis_table]

            artificial_basis_result = None

            while True:
                artificial_basis_result = self.symplex_step(old_symplex_table=self.steps[0][-1], artificial_basis_method=True)
                if isinstance(artificial_basis_result, list):
                    self.steps[0].append(artificial_basis_result)
                elif isinstance(artificial_basis_result, tuple):
                    artificial_basis_result = artificial_basis_result[0]
                    break

            if artificial_basis_result is not None:
                gauss_art_table = self.convert_art_table(task_matrix[0], artificial_basis_result)
                reduced_function = self.reduce_function(task_matrix[0], gauss_art_table[0], gauss_art_table[1], extremum_type)

                print('\nИтог минимизации:')
                for i in reduced_function:
                    print(i, end=' ')
                print()
                print()

                initial_symplex_table = self.create_initial_symplex_table_for_art(artificial_basis_result, reduced_function)

                self.steps[1] = [initial_symplex_table]

                print('Симплекс метод!\n')

                while True:
                    symplex_result = self.symplex_step(self.steps[1][-1])
                    if isinstance(symplex_result, list):
                        self.steps[1].append(symplex_result)
                    elif isinstance(symplex_result, tuple):
                        self.result.function_result = symplex_result[0]
                        self.result.basis_result = symplex_result[1]
                        self.result.comment = "Задача успешно решена!"

                        return symplex_result
                    elif symplex_result is None:
                        return symplex_result
            else:
                print('Ошибка во время выполнения метода иск базиса!')
                return None
        else:
            print('Ошибка! Кол-во выбранных базисных переменных != кол-ву ограничений!')
            return None

    def create_initial_symplex_table_for_art(self, art_result, reduced_function):
        s_t = [['x(0)']]
        not_basis_vars = []

        # Добавляем оглавление с не базисными переменными
        for col_index in range(1, len(art_result[0])):
            not_basis_vars.append(int(''.join(list(art_result[0][col_index][1:]))))
            s_t[0].append(art_result[0][col_index])

        for row_index in range(1, len(art_result) - 1):
            s_t.append(art_result[row_index])

        s_t.append(['f'])
        for basis_var in not_basis_vars:
            s_t[-1].append(reduced_function[basis_var - 1])

        s_t[-1].append(reduced_function[-1] * -1)

        return s_t

    def convert_art_table(self, function, art_table):
        print('Перестроение таблицы после метода искуственного базиса для минимизации функции...')

        art_copy = []

        for row in art_table:
            new_art_row = []
            for el in row:
                new_art_row.append(el)
            art_copy.append(new_art_row)

        basis_vars = []
        not_basis_vars = []
        for row_index in range(1, len(art_copy) - 1):
            var = int(''.join(list(art_copy[row_index][0])[1:]))
            basis_vars.append(var)

        # for col_index in range(1, len(art_copy[0])):
        for i in range(len(function)):
            el_num = i + 1
            if el_num not in basis_vars:
                not_basis_vars.append(el_num)

        art_short_matrix = []
        for row_index in range(1, len(art_copy) - 1):
            art_short_matrix.append(art_copy[row_index])

        art_short_matrix.sort(key = lambda x: x[0])

        gauss_matrix = []
        for art_short_row in art_short_matrix:
            basis_var = int(''.join(list(art_short_row[0])[1:]))

            # target_row_len = len(basis_vars) + len(not_basis_vars) + 1

            gauss_matrix_row = [None for _ in range(max(basis_vars + not_basis_vars) + 1)]

            for i in range(len(art_short_row)):
                if isinstance(art_short_row[i], str):
                    art_short_row.pop(i)
                    break

            for i in range(len(not_basis_vars)):
                gauss_index = not_basis_vars[i] - 1
                gauss_value = art_short_row[i]
                gauss_matrix_row[gauss_index] = gauss_value

            gauss_matrix_row[-1] = art_short_row[-1]

            gauss_matrix_row[basis_var - 1] = Fraction(1)

            for another_basis_var in basis_vars:
                if another_basis_var != basis_var:
                    gauss_matrix_row[another_basis_var - 1] =  Fraction(0)

            gauss_matrix.append(gauss_matrix_row)

        print('Итоговая единичная матрица:')
        for row in gauss_matrix:
            print(*row)

        basis_indexes = [0] * (len(function))
        for i in range(len(basis_indexes)):
            var = i + 1
            if var in basis_vars:
                basis_indexes[i] = 1

        return gauss_matrix, basis_indexes
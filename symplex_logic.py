from array import ArrayType
from fractions import Fraction

from task_config import ExtremumType, SolutionType


class SymplexStep:
    def __init__(self):
        self.matrix = []
        self.support_element = []
        self.available_support_elements = []

class SymplexLogic:
    def __init__(self):
        self.steps = []

    def gauss_method(self, matrix, target_columns):
        rows = len(matrix)
        num_columns = len(matrix[0])

        # Приведение диагонального элемента к 1 (нормировка)
        for row_index, col_index in enumerate(target_columns):
            # Элемент, который должен стать единичным
            pivot = matrix[row_index][col_index]

            # Делим все оставшиеся элементы строки, чтобы привести элемент к 1
            for j in range(num_columns):
                matrix[row_index][j] /= pivot

            # Длаее для каждой строки (без pivot)
            for target_row in range(rows):
                if target_row != row_index:
                    factor = matrix[target_row][col_index]
                    for column in range(num_columns):
                        # Вычитаем factor кол-во строк pivot элемента, чтобы привести весь стобец под ним в единичную матрицу
                        matrix[target_row][column] -= factor * matrix[row_index][column]
        return matrix

    def reduced_function(self, function, gauss_matrix, basis, extremum_type):
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

    def get_initial_symplex_table(self, reduced_function, gauss_matrix, basis, extremum_type):
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
                new_symplex_row.append(gauss_matrix[gauss_row][not_basis_index])
            new_symplex_row.append(gauss_matrix[gauss_row][-1])
            gauss_row += 1
            symplex_table.append(new_symplex_row)

        final_symplex_row = ['f']
        for not_basis_index in not_basis_indexes:
                final_symplex_row.append(reduced_function[not_basis_index])
        final_symplex_row.append(reduced_function[-1] * -1)
        symplex_table.append(final_symplex_row)

        return symplex_table

    def artificial_basis_method(self):
        pass

    # st = symplex_table
    def solve_task(self, st, extremum_type, solution_type):
        self.steps = [st]



        while True:
            old_st = self.steps[-1]
            new_st = []

            # Делаем глубокую копию последней симплекс-таблицы
            print('Симплекс-таблица:')
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
            sorted_available_col_coeffs = dict(sorted(available_col_coeffs.items(), key=lambda item: item[1]))

            if len(sorted_available_col_coeffs) == 0:
                print('Нет доступных столбцов для выбора, симплекс метод закончен!\n')
                result = new_st[-1][-1]
                if extremum_type == ExtremumType.MIN:
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

            if solution_type == SolutionType.AUTO:
                support_element = sorted_available_support_elements[0]
            elif solution_type == SolutionType.MANUAL:
                print('Выберите опорный элемент:')
                for el in sorted_available_support_elements:
                    print(el[0], f'Строка: {el[-2]}', f'Столбец: {el[-1]}')

                s_el_address = input('\nВведите строку и стобец опорного элемента, ex: "2 1" (Enter для выбора наилучшего): ')

                if s_el_address == '':
                    support_element = sorted_available_support_elements[0]
                else:
                    s_el_address = [int(_) for _ in s_el_address.split(' ')]
                    for el in sorted_available_support_elements:
                        if s_el_address == [el[-2], el[-1]]:
                            support_element = el
                            break
                    if support_element is None:
                        support_element = sorted_available_support_elements[0]

            if support_element is None:
                return None

            print(f'Выбран: {str(support_element)}\n')

            support_el_value = support_element[0]
            support_col_index = support_element[-1]
            support_row_index = support_element[-2]

            # Нулевой шаг симплекс метода
            # Xi -> Xi+1
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

            self.steps.append(new_st)


    def generate_basis_output(self, st):
        basis_arr = [Fraction(0)] * ((len(st) - 2) + (len(st[0]) - 1))
        for row_index in range(1, len(st) - 1):
            literals = [i for i in st[row_index][0]]
            var_index = ''
            for i in range(1, len(literals)):
                var_index += literals[i]
            basis_arr[int(var_index)-1] = st[row_index][-1]
        return basis_arr


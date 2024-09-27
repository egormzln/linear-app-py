from fractions import Fraction

from task_config import ExtremumType

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

        first_symplex_row = ['x0']
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

    def solve_task(self, symplex_table, extremum_type):
        # Сначала находим опорные элементы

        # {'Столбец': '<Значение>'}
        available_col_coeffs = {}
        for i in range(1, len(symplex_table[-1]) - 1):
            available_col_coeffs[i] = symplex_table[-1][i]
        sorted_available_col_coeffs = dict(sorted(available_col_coeffs.items(), key=lambda item: item[1]))

        available_support_elements = []
        for col_index in sorted_available_col_coeffs.keys():
            for row_index in range(1, len(symplex_table) - 1):
                if symplex_table[row_index][col_index] > 0:
                    new_support_element = symplex_table[row_index][col_index]
                    simplex_relation = symplex_table[row_index][-1] / symplex_table[row_index][col_index]
                    available_support_elements.append([new_support_element, simplex_relation, row_index, col_index])
        sorted_available_support_elements = sorted(available_support_elements, key=lambda x: x[1])

        if len(sorted_available_support_elements) != 0:
            print('Наилучший опорный элемент')
            print(sorted_available_support_elements[0])
        else:
            print('Опорные элементы отсутсвуют')
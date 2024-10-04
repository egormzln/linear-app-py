from enum import Enum
from fractions import Fraction

from PySide6 import QtCore


class SolutionType(Enum):
    AUTO = 'Авто'
    MANUAL = 'Шаг за шагом'


class TypeOfFractions(Enum):
    COMMON = 'Обычные'
    DECIMAL = 'Десятичные'


class ExtremumType(Enum):
    MIN = 'Минимизировать'
    MAX = 'Максимизировать'


class TaskConfig:
    def __init__(self):
        self.var_count = 5
        self.limits_count = 3
        self.solution_type = SolutionType.MANUAL
        self.type_of_fractions = TypeOfFractions.COMMON
        self.extremum_type = ExtremumType.MIN
        self.input_matrix = self._gen_default_matrix()

    def set_var_count(self, new_var_count):
        self.var_count = new_var_count

    def set_limits_count(self, new_limits_count):
        self.limits_count = new_limits_count

    def set_matrix_element(self, x, y, value):
        self.input_matrix[x][y] = value
        print(self.input_matrix)

    def set_solution_type(self, new_solution_type):
        self.solution_type = new_solution_type

    def set_type_of_fractions(self, new_type_of_fractions):
        self.type_of_fractions = new_type_of_fractions

    def set_extremum_type(self, new_extremum_type):
        self.extremum_type = new_extremum_type

    def update_matrix_length(self):
        self.input_matrix = self._gen_default_matrix()

    def show_fraction(self):
        return self.type_of_fractions.name == self.type_of_fractions.COMMON.name

    def _gen_default_matrix(self):
        self.default_matrix_value = Fraction(0)
        self.new_default_matrix = []
        for i in range(self.limits_count + 2):
            new_matrix_row = []
            for j in range(self.var_count + 1):
                # Не добавляем последний элемент первой строки тк у функции нет начального значения
                if i in [0, self.limits_count + 1] and j == self.var_count:
                    continue
                new_matrix_row.append(self.default_matrix_value)
            self.new_default_matrix.append(new_matrix_row)
        print(self.new_default_matrix)
        return self.new_default_matrix
        # return [[self.default_matrix_value for _ in range(self.var_count + 1)] for _ in range(self.limits_count + 2)]

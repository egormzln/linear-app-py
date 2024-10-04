from fractions import Fraction

from PySide6 import QtCore

from task_config import TaskConfig


class MatrixModel(QtCore.QAbstractTableModel):
    def __init__(self, var_count: int, limits_count: int, task_config: TaskConfig, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.column_count = var_count + 2
        self.row_count = limits_count + 3 + 1
        self._task_config = task_config

    def set_items(self):
        pass

    def columnCount(self, parent=...):
        return self.column_count

    def rowCount(self, parent=...):
        return self.row_count

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        elif role == QtCore.Qt.ItemDataRole.DisplayRole:
            if (index.row(), index.column()) in [(0, 0), (2, 0)] \
                    or ((index.row() in [0, 1]) and index.column() == self.column_count - 1) \
                    or (index.row() == self.row_count - 1 and index.column() == self.column_count - 1):
                return ''
            elif index.row() == self.column_count - 1 and index.column() == 0:
                return 'Базис'
            elif index.row() == 0 and 0 < index.column() < self.column_count - 1:
                return f'c{index.column()}'
            elif index.column() == 0 and index.row() == 1:
                return 'f(x)'
            elif index.column() == 0 and index.row() > 1:
                return f'f{index.row()-2}(x)'
            elif index.row() == 2 and 0 < index.column() < self.column_count - 1:
                return f'a{index.column()}'
            elif index.row() == 2 and index.column() == self.column_count - 1:
                return 'b'
            else:
                if index.row() == 1:
                    show_value = None
                    if self._task_config.show_fraction():
                        show_value = str(self._task_config.input_matrix[0][index.column()-1])
                    else:
                        show_value = str(round(float(self._task_config.input_matrix[0][index.column()-1]), 3))
                    return show_value
                else:
                    show_value = None
                    if self._task_config.show_fraction():
                        show_value = str(self._task_config.input_matrix[index.row()-2][index.column()-1])
                    else:
                        show_value = str(round(float(self._task_config.input_matrix[index.row()-2][index.column()-1]), 3))
                    return show_value

        elif role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            if (index.row(), index.column()) in [(0, 0), (2, 0)]:
                return QtCore.Qt.AlignmentFlag.AlignCenter
            elif index.row() == 0 and 0 < index.column() < self.column_count - 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter
            elif index.row() == 0 and index.column() == self.column_count - 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter
            elif index.column() == 0 and index.row() == 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter
            elif index.column() == 0 and index.row() > 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter
            elif index.row() == 2 and 0 < index.column() < self.column_count - 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter
            elif index.row() == 2 and index.column() == self.column_count - 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter

    def setData(self, index, value, role):
        if role == QtCore.Qt.ItemDataRole.EditRole:
            if index.row() == 1:
                new_value = Fraction(value)
                self._task_config.set_matrix_element(index.row()-1, index.column()-1, new_value)
                return True
            elif index.row() == self.row_count - 1:
                if value == "0" or value == "1":
                    new_value = Fraction(value)
                    self._task_config.set_matrix_element(index.row() - 2, index.column() - 1, new_value)
                    return True
                return False
            else:
                new_value = Fraction(value)
                self._task_config.set_matrix_element(index.row()-2, index.column()-1, new_value)
                return True

    def flags(self, index):
        if index.column() == 0 or index.row() in [0, 2] \
                or (index.column() == self.column_count - 1 and index.row() in [0, 1, self.row_count - 1]):
            return QtCore.Qt.ItemFlag.NoItemFlags
        return QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsEditable


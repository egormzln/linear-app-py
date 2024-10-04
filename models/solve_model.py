from PySide6 import QtCore

from symplex_logic import SymplexLogic
from task_config import TaskConfig


class SolveModel(QtCore.QAbstractTableModel):
    def __init__(self, var_count: int, limits_count: int, task_config: TaskConfig, symplex_logic: SymplexLogic, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.column_count = 5
        self.row_count = 5
        self.task_config = task_config
        self.symplex_logic = symplex_logic

# Тут вывести надо начальную симплекс таблицу
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        elif role == QtCore.Qt.ItemDataRole.DisplayRole:
            return 'a'


    def set_items(self):
        pass

    def columnCount(self, parent=...):
        return self.column_count

    def rowCount(self, parent=...):
        return self.row_count

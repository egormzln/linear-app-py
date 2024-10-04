from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt

from symplex_logic import SymplexLogic
from task_config import TaskConfig, TypeOfFractions
from test import available_support_elements


class SymplexStep:
    def __init__(self, table, available_support_elements):
        self.table = table
        self.available_support_elements = available_support_elements
        self.is_finished = False

class ArtificialBasisStep:
    def __init__(self, table, available_support_elements):
        self.table = table
        self.available_support_elements = available_support_elements
        self.is_finished = False


class SolveModel(QtCore.QAbstractTableModel):
    def __init__(self, task_config: TaskConfig, symplex_logic: SymplexLogic, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.symplex_logic = symplex_logic
        self.task_config = task_config
        self.steps = []
        # [ <Метод: 0 - иск базис / 1 - симплекс>, <Индекс шага в методе> ]
        self.current_step_index = 0

        if len(self.steps) == 0:
            task_matrix = self.task_config.input_matrix
            basis_vars = self.symplex_logic.get_basis_vars(task_matrix)
            if len(basis_vars) != 0:
                initial_symplex_table = self.symplex_logic.get_initial_symplex_table(
                    task_matrix=task_matrix,
                    basis_vars=self.symplex_logic.get_basis_vars(task_matrix),
                    extremum_type=self.task_config.extremum_type
                )
                available_support_elements = self.symplex_logic.get_available_support_elements(initial_symplex_table)
                self.steps.append(
                    SymplexStep(
                        initial_symplex_table,
                        available_support_elements
                    )
                )
            else:
                initial_art_table = self.symplex_logic.get_init_artificial_basis_table(task_matrix)
                available_support_elements = self.symplex_logic.get_available_support_elements(initial_art_table)
                self.steps.append(
                    ArtificialBasisStep(
                        initial_art_table,
                        available_support_elements
                    )
                )

        self.column_count = len(self.steps[0].table[0]) + 1
        self.row_count = len(self.steps[0].table)

    def next_step(self, selected_support_element):
        last_step = self.steps[-1]
        if not last_step.is_finished:
            next_step_result = None
            if last_step is SymplexStep:
                next_step_result = self.symplex_logic.symplex_step(last_step, selected_support_element)
            # elif last_step is ArtificialBasisStep:
                # next_step_result = self.symplex_logic.artificial_basis_method(last_step, selected_support_element)

            # if isinstance(next_step_result, list):
            #
            #     self.steps.append(
            # elif isinstance(symplex_result, tuple):
            #     self.result.function_result = symplex_result[0]
            #     self.result.basis_result = symplex_result[1]
            #     self.result.comment = "Задача успешно решена!"
            #
            #     return symplex_result
            # elif symplex_result is None:
            #     return symplex_result
            #


    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return

        row, col = index.row(), index.column()

        available_support_element_tuples = []
        for support_element in self.steps[self.current_step_index].available_support_elements:
            available_support_element_tuples.append((support_element[-2], support_element[-1]))

        # Handle background highlighting based on condition
        if role == QtCore.Qt.ItemDataRole.BackgroundRole:
            if len(available_support_element_tuples) == 0:
                pass
            elif (row, col) == available_support_element_tuples[0]:
                return QtGui.QColor(3, 138, 255, 150) # Highlight specific cells
            elif (row, col) in available_support_element_tuples[1:]:
                return QtGui.QColor(3, 138, 255, 70)

        elif role == QtCore.Qt.ItemDataRole.DisplayRole:
            ct = self.steps[self.current_step_index].table
            try:
                if self.task_config.type_of_fractions == TypeOfFractions.COMMON:
                    return str(ct[index.row()][index.column()])
                elif self.task_config.type_of_fractions == TypeOfFractions.DECIMAL:
                    return str(round(float(ct[index.row()][index.column()]), 3))
            except:
                return None


    def set_items(self):
        pass

    def columnCount(self, parent=...):
        return self.column_count

    def rowCount(self, parent=...):
        return self.row_count

    def flags(self, index):

        if self.check_table_element(index):
            return QtCore.Qt.ItemFlag.ItemIsEnabled
        return QtCore.Qt.ItemFlag.NoItemFlags

    def check_table_element(self, index):
        row, col = index.row(), index.column()

        available_support_element_tuples = []
        for support_element in self.steps[self.current_step_index].available_support_elements:
            available_support_element_tuples.append((support_element[-2], support_element[-1]))

        return (row, col) in available_support_element_tuples


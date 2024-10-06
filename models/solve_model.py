from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt

from symplex_logic import SymplexLogic
from task_config import TaskConfig, TypeOfFractions, ExtremumType
from test import available_support_elements


class SymplexStep:
    def __init__(self, table, available_support_elements, is_finished=False):
        self.table = table
        self.available_support_elements = available_support_elements
        self.is_finished = is_finished

class ArtificialBasisStep:
    def __init__(self, table, available_support_elements, is_finished=False):
        self.table = table
        self.available_support_elements = available_support_elements
        self.is_finished = is_finished


class SolveModel(QtCore.QAbstractTableModel):
    def __init__(self, task_config: TaskConfig, symplex_logic: SymplexLogic, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.symplex_logic = symplex_logic
        self.task_config = task_config
        self.steps = []
        # [ <Метод: 0 - иск базис / 1 - симплекс>, <Индекс шага в методе> ]
        self.current_step_index = 0
        self.solving_is_ended = False

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
        next_step_result = None

        if isinstance(last_step, SymplexStep):
            next_step_result = self.symplex_logic.symplex_step(last_step.table, selected_support_element)
            available_support_elements = self.symplex_logic.get_available_support_elements(next_step_result)

            if len(available_support_elements) != 0:
                self.steps.append(
                    SymplexStep(
                        table=next_step_result,
                        available_support_elements=available_support_elements
                    )
                )
                self.layoutChanged.emit()
            else:
                self.steps.append(
                    SymplexStep(
                        table=next_step_result,
                        available_support_elements=available_support_elements,
                        is_finished=True
                    )
                )
                result = next_step_result[-1][-1]

                if self.task_config.extremum_type == ExtremumType.MIN.name:
                    result *= -1
                basis = self.symplex_logic.generate_basis_output(next_step_result)

                self.symplex_logic.result.function_result = result
                self.symplex_logic.result.basis_result = basis
                self.symplex_logic.result.comment = "Задача успешно решена!"

                self.solving_is_ended = True

        elif isinstance(last_step, ArtificialBasisStep):
            if not last_step.is_finished:
                next_step_result = self.symplex_logic.symplex_step(
                    last_step.table,
                    selected_support_element,
                    True
                )
                available_support_elements = self.symplex_logic.get_available_support_elements(next_step_result)

                if len(available_support_elements) != 0:
                    self.steps.append(
                        ArtificialBasisStep(
                            table=next_step_result,
                            available_support_elements=available_support_elements
                        )
                    )
                    self.layoutChanged.emit()
                else:
                    gauss_art_table = self.symplex_logic.convert_art_table(self.task_config.input_matrix[0], next_step_result)
                    reduced_function = self.symplex_logic.reduce_function(
                        self.task_config.input_matrix[0],
                        gauss_art_table[0],
                        gauss_art_table[1],
                        self.task_config.extremum_type
                    )
                    initial_symplex_table = self.symplex_logic.create_initial_symplex_table_for_art(
                        next_step_result,
                        reduced_function
                    )
                    available_support_elements = self.symplex_logic.get_available_support_elements(initial_symplex_table)
                    self.steps.append(
                        SymplexStep(
                            table=initial_symplex_table,
                            available_support_elements=available_support_elements
                        )
                    )
                    self.layoutChanged.emit()

        self.current_step_index += 1

    def _next_step_available(self, table):
        sup_elements = self.symplex_logic.get_available_support_elements(table)

        if len(sup_elements) == 0:
            return False


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

    def back_step(self):
        self.steps.pop()
        self.current_step_index -= 1
        self.layoutChanged.emit()

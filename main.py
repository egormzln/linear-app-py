import sys
from fractions import Fraction

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from models.matrix_model import MatrixModel
from models.solve_model import SolveModel
from res.ui.py.answer_dialog import Ui_AnswerDialog
from res.ui.py.main_screen import Ui_MainWindow
from res.ui.py.info_dialog import Ui_InfoDialog
from res.ui.py.new_matrix_dialog import Ui_TaskInputDialog
from res.ui.py.instruction_dialog import Ui_InstructionDialog
from res.ui.py.solution_dialog import Ui_SolvingDialog
from symplex_logic import SymplexLogic
from task_config import TaskConfig, TypeOfFractions, SolutionType, ExtremumType


class LinearApp(QMainWindow):
    def __init__(self):
        super(LinearApp, self).__init__()

        self.task_config = TaskConfig()

        self.symplex_logic = SymplexLogic()

        self.matrix_model, self.new_window, self.ui_window = None, None, None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup QSpinBox value
        self.ui.input_count_limits.setValue(self.task_config.limits_count)
        self.ui.input_count_variables.setValue(self.task_config.var_count)

        # Меню бар
        self.ui.action_info.triggered.connect(self, self.open_info_dialog)
        self.ui.action_instruction.triggered.connect(self, self.open_instruction_dialog)
        self.ui.action_load_from_file.triggered.connect(self, self.load_from_file)

        # Кнопка далее
        self.ui.btn_next.clicked.connect(self.open_input_task_matrix)

        # Радио тип задачи
        self.ui.radio_tot_min.setText(ExtremumType.MIN.value)
        self.ui.radio_tot_max.setText(ExtremumType.MAX.value)
        self.ui.radio_tot_min.toggled.connect(self.on_tot_radio_toggled)

        # Радио тип дробей
        self.ui.radio_tof_default.toggled.connect(self.on_tof_radio_toggled)

        # Радио тип решения
        self.ui.radio_st_auto.toggled.connect(self.on_st_radio_toggled)

    def on_tot_radio_toggled(self):
        if self.ui.radio_tot_min.isChecked():
            self.task_config.set_extremum_type(ExtremumType.MIN)
        elif self.ui.radio_tot_max.isChecked():
            self.task_config.set_extremum_type(ExtremumType.MAX)
        print(f"Тип задачи: {self.task_config.extremum_type.value}")

    def on_tof_radio_toggled(self):
        if self.ui.radio_tof_default.isChecked():
            self.task_config.set_type_of_fractions(TypeOfFractions.COMMON)
        elif self.ui.radio_tof_decimal.isChecked():
            self.task_config.set_type_of_fractions(TypeOfFractions.DECIMAL)
        print(f"Тип дробей: {self.task_config.type_of_fractions.value}")

    def on_st_radio_toggled(self):
        if self.ui.radio_st_auto.isChecked():
            self.task_config.set_solution_type(SolutionType.AUTO)
        else:
            self.task_config.set_solution_type(SolutionType.MANUAL)
        print(f"Тип решения: {self.task_config.solution_type.value}")

    def open_input_task_matrix(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_TaskInputDialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        self.ui_window.btn_cancel.clicked.connect(self.new_window.close)
        self.ui_window.btn_start_solving.clicked.connect(self.open_solve_dialog)

        # Update TaksConfig
        text_field_var_count = int(self.ui.input_count_variables.text())
        text_field_limits_count = int(self.ui.input_count_limits.text())
        if self.task_config.var_count != text_field_var_count or self.task_config.limits_count != text_field_limits_count:
            self.task_config.set_var_count(int(self.ui.input_count_variables.text()))
            self.task_config.set_limits_count(int(self.ui.input_count_limits.text()))
            self.task_config.update_matrix_length()

        # Create Matrix Model
        self.matrix_model = MatrixModel(var_count=self.task_config.var_count, limits_count=self.task_config.limits_count, task_config=self.task_config)
        self.ui_window.matrix_task_input.setModel(self.matrix_model)

    def open_solve_dialog(self):
        if self.task_config.solution_type == SolutionType.AUTO:
            self.symplex_logic.solve_task(task_matrix=self.task_config.input_matrix,
                                          solution_type=self.task_config.solution_type,
                                          extremum_type=self.task_config.solution_type)
            self.new_window.close()
            self._open_result_dialog()
        elif self.task_config.solution_type == SolutionType.MANUAL:
            self.new_window.close()

            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_SolvingDialog()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()

            self.matrix_model = SolveModel(var_count=self.task_config.var_count,
                                           limits_count=self.task_config.limits_count,
                                           symplex_logic=self.symplex_logic,
                                           task_config=self.task_config)
            self.ui_window.task_matrix.setModel(self.matrix_model)

    def _open_result_dialog(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_AnswerDialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        self.ui_window.btn_answer_ok.clicked.connect(self.new_window.close)

        self.ui_window.lbl_task_status.setText(self.symplex_logic.result.comment)

        basis_output = "x* ( "
        for el in self.symplex_logic.result.basis_result:
            if self.task_config.type_of_fractions == TypeOfFractions.COMMON:
                basis_output += str(el) + " "
            else:
                basis_output += str(round(float(el), 3)) + " "
        basis_output += ")"

        function_output = "f* = "
        if self.task_config.type_of_fractions == TypeOfFractions.COMMON:
            function_output += str(self.symplex_logic.result.function_result)
        else:
            function_output += str(round(float(self.symplex_logic.result.function_result), 3))

        result_output = f"{basis_output}\n{function_output}"

        self.ui_window.lbl_answer.setText(result_output)

    def open_info_dialog(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_InfoDialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        self.ui_window.btn_info_close.clicked.connect(self.new_window.close)

    def open_instruction_dialog(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_InstructionDialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        self.ui_window.btn_instruction_close.clicked.connect(self.new_window.close)

    def load_from_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл задачи", "res/tasks", "Text Files (*.txt)")

        # If a file is selected, print its path
        if file_path:
            try:
                print(f"Selected file: {file_path}")
                file = open(file_path, "r")
                file_data = file.readlines()
                file.close()

                new_task_matrix = []

                for row_index in range(len(file_data) - 1):
                    new_row = [Fraction(i) for i in file_data[row_index].split(',')]
                    new_task_matrix.append(new_row)

                self.task_config.set_type_of_fractions(TypeOfFractions.COMMON)

                self.task_config.set_var_count(len(new_task_matrix[0]))
                self.task_config.set_limits_count(len(new_task_matrix) - 2)

                self.ui.input_count_variables.setValue(self.task_config.var_count)
                self.ui.input_count_limits.setValue(self.task_config.limits_count)

                self.task_config.set_extremum_type(str(file_data[-1]).upper())
                self.task_config.input_matrix = new_task_matrix

                print('Данные из файла успешно прочитаны!')
            except:
                print('Ошибка чтения файла!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinearApp()
    window.show()
    sys.exit(app.exec())

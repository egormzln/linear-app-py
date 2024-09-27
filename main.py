import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from res.ui.py.main_screen import Ui_MainWindow
from res.ui.py.info_dialog import Ui_InfoDialog
from res.ui.py.new_matrix_dialog import Ui_TaskInputDialog
from res.ui.py.instruction_dialog import Ui_InstructionDialog
from task_config import MatrixItems, TaskConfig, TypeOfFractions, SolutionType, ExtremumType


class LinearApp(QMainWindow):
    def __init__(self):
        super(LinearApp, self).__init__()

        self.task_config = TaskConfig()

        self.matrix_model, self.new_window, self.ui_window = None, None, None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup QSpinBox value
        self.ui.input_count_limits.setValue(self.task_config.limits_count)
        self.ui.input_count_variables.setValue(self.task_config.var_count)

        # Меню бар
        self.ui.action_info.triggered.connect(self, self.open_info_dialog)
        self.ui.action_instruction.triggered.connect(self, self.open_instruction_dialog)

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

        # Update TaksConfig
        self.task_config.set_var_count(int(self.ui.input_count_variables.text()))
        self.task_config.set_limits_count(int(self.ui.input_count_limits.text()))
        self.task_config.update_matrix_length()

        # Create Matrix Model
        self.matrix_model = MatrixItems(var_count=self.task_config.var_count, limits_count=self.task_config.limits_count, task_config=self.task_config)
        self.ui_window.matrix_task_input.setModel(self.matrix_model)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinearApp()
    window.show()
    sys.exit(app.exec())

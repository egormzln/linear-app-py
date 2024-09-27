# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(259, 424)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(259, 424))
        MainWindow.setMaximumSize(QSize(259, 424))
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"")
        self.action_load_from_file = QAction(MainWindow)
        self.action_load_from_file.setObjectName(u"action_load_from_file")
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.action_instruction = QAction(MainWindow)
        self.action_instruction.setObjectName(u"action_instruction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20pt;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_count_variables = QLabel(self.centralwidget)
        self.lbl_count_variables.setObjectName(u"lbl_count_variables")

        self.horizontalLayout_3.addWidget(self.lbl_count_variables)

        self.input_count_variables = QSpinBox(self.centralwidget)
        self.input_count_variables.setObjectName(u"input_count_variables")
        self.input_count_variables.setMinimum(2)
        self.input_count_variables.setMaximum(16)
        self.input_count_variables.setValue(5)

        self.horizontalLayout_3.addWidget(self.input_count_variables)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 12)
        self.lbl_count_limits = QLabel(self.centralwidget)
        self.lbl_count_limits.setObjectName(u"lbl_count_limits")

        self.horizontalLayout_2.addWidget(self.lbl_count_limits)

        self.input_count_limits = QSpinBox(self.centralwidget)
        self.input_count_limits.setObjectName(u"input_count_limits")
        self.input_count_limits.setMinimum(1)
        self.input_count_limits.setMaximum(15)
        self.input_count_limits.setValue(4)

        self.horizontalLayout_2.addWidget(self.input_count_limits)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.group_type_of_task = QGroupBox(self.centralwidget)
        self.group_type_of_task.setObjectName(u"group_type_of_task")
        self.group_type_of_task.setStyleSheet(u"")
        self.group_type_of_task.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.group_type_of_task)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.radio_tot_min = QRadioButton(self.group_type_of_task)
        self.radio_tot_min.setObjectName(u"radio_tot_min")
        self.radio_tot_min.setCheckable(True)
        self.radio_tot_min.setChecked(True)

        self.verticalLayout.addWidget(self.radio_tot_min)

        self.radio_tot_max = QRadioButton(self.group_type_of_task)
        self.radio_tot_max.setObjectName(u"radio_tot_max")

        self.verticalLayout.addWidget(self.radio_tot_max)


        self.verticalLayout_2.addWidget(self.group_type_of_task)

        self.group_type_of_fractions = QGroupBox(self.centralwidget)
        self.group_type_of_fractions.setObjectName(u"group_type_of_fractions")
        self.group_type_of_fractions.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.group_type_of_fractions)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.radio_tof_default = QRadioButton(self.group_type_of_fractions)
        self.radio_tof_default.setObjectName(u"radio_tof_default")
        self.radio_tof_default.setChecked(True)

        self.verticalLayout_3.addWidget(self.radio_tof_default)

        self.radio_tof_decimal = QRadioButton(self.group_type_of_fractions)
        self.radio_tof_decimal.setObjectName(u"radio_tof_decimal")

        self.verticalLayout_3.addWidget(self.radio_tof_decimal)


        self.verticalLayout_2.addWidget(self.group_type_of_fractions)

        self.group_solution_type = QGroupBox(self.centralwidget)
        self.group_solution_type.setObjectName(u"group_solution_type")
        self.group_solution_type.setFlat(True)
        self.verticalLayout_4 = QVBoxLayout(self.group_solution_type)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.radio_st_step_by_step = QRadioButton(self.group_solution_type)
        self.radio_st_step_by_step.setObjectName(u"radio_st_step_by_step")
        self.radio_st_step_by_step.setChecked(True)

        self.verticalLayout_4.addWidget(self.radio_st_step_by_step)

        self.radio_st_auto = QRadioButton(self.group_solution_type)
        self.radio_st_auto.setObjectName(u"radio_st_auto")

        self.verticalLayout_4.addWidget(self.radio_st_auto)


        self.verticalLayout_2.addWidget(self.group_solution_type)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_next = QPushButton(self.centralwidget)
        self.btn_next.setObjectName(u"btn_next")

        self.horizontalLayout.addWidget(self.btn_next)

        self.horizontalSpacer = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_menu_bar = QMenuBar(MainWindow)
        self.main_menu_bar.setObjectName(u"main_menu_bar")
        self.main_menu_bar.setEnabled(True)
        self.main_menu_bar.setGeometry(QRect(0, 0, 259, 24))
        self.main_menu_bar.setDefaultUp(True)
        self.main_menu_bar.setNativeMenuBar(True)
        self.file_menu = QMenu(self.main_menu_bar)
        self.file_menu.setObjectName(u"file_menu")
        self.info_menu = QMenu(self.main_menu_bar)
        self.info_menu.setObjectName(u"info_menu")
        MainWindow.setMenuBar(self.main_menu_bar)

        self.main_menu_bar.addAction(self.file_menu.menuAction())
        self.main_menu_bar.addAction(self.info_menu.menuAction())
        self.file_menu.addAction(self.action_load_from_file)
        self.info_menu.addAction(self.action_instruction)
        self.info_menu.addAction(self.action_info)

        self.retranslateUi(MainWindow)

        self.btn_next.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.action_load_from_file.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_instruction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.lbl_count_variables.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0427\u0438\u0441\u043b\u043e \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445:</span></p></body></html>", None))
        self.lbl_count_limits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0427\u0438\u0441\u043b\u043e \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439:</span></p></body></html>", None))
        self.group_type_of_task.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438:", None))
        self.radio_tot_min.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0443\u043c", None))
        self.radio_tot_max.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c", None))
        self.group_type_of_fractions.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0434\u0440\u043e\u0431\u0435\u0439:", None))
        self.radio_tof_default.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044b\u0447\u043d\u044b\u0435", None))
        self.radio_tof_decimal.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0441\u044f\u0442\u0438\u0447\u043d\u044b\u0435", None))
        self.group_solution_type.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u0448\u0435\u043d\u0438\u044f:", None))
        self.radio_st_step_by_step.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0430\u0433\u043e\u0432\u044b\u0439", None))
        self.radio_st_auto.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.info_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi


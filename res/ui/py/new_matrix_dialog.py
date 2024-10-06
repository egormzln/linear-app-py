# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_matrix_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_TaskInputDialog(object):
    def setupUi(self, TaskInputDialog):
        if not TaskInputDialog.objectName():
            TaskInputDialog.setObjectName(u"TaskInputDialog")
        TaskInputDialog.resize(709, 456)
        self.verticalLayout_2 = QVBoxLayout(TaskInputDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.matrix_task_input = QTableView(TaskInputDialog)
        self.matrix_task_input.setObjectName(u"matrix_task_input")
        self.matrix_task_input.horizontalHeader().setVisible(False)
        self.matrix_task_input.horizontalHeader().setHighlightSections(False)
        self.matrix_task_input.verticalHeader().setVisible(False)
        self.matrix_task_input.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.matrix_task_input)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(TaskInputDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_cancel.setStyleSheet(u"color: rgb(255, 38, 0);")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_start_solving = QPushButton(TaskInputDialog)
        self.btn_start_solving.setObjectName(u"btn_start_solving")
        self.btn_start_solving.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_start_solving.setStyleSheet(u"")
        self.btn_start_solving.setCheckable(False)
        self.btn_start_solving.setAutoExclusive(False)
        self.btn_start_solving.setAutoDefault(True)
        self.btn_start_solving.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_start_solving)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(TaskInputDialog)

        self.btn_start_solving.setDefault(False)


        QMetaObject.connectSlotsByName(TaskInputDialog)
    # setupUi

    def retranslateUi(self, TaskInputDialog):
        TaskInputDialog.setWindowTitle(QCoreApplication.translate("TaskInputDialog", u"\u0412\u0432\u043e\u0434 \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_cancel.setText(QCoreApplication.translate("TaskInputDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btn_start_solving.setText(QCoreApplication.translate("TaskInputDialog", u"\u0420\u0435\u0448\u0438\u0442\u044c", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solution_dialog.ui'
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

class Ui_SolvingDialog(object):
    def setupUi(self, SolvingDialog):
        if not SolvingDialog.objectName():
            SolvingDialog.setObjectName(u"SolvingDialog")
        SolvingDialog.resize(683, 437)
        self.verticalLayout_2 = QVBoxLayout(SolvingDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.task_matrix = QTableView(SolvingDialog)
        self.task_matrix.setObjectName(u"task_matrix")
        self.task_matrix.horizontalHeader().setVisible(False)
        self.task_matrix.horizontalHeader().setHighlightSections(False)
        self.task_matrix.verticalHeader().setVisible(False)
        self.task_matrix.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.task_matrix)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_step_back = QPushButton(SolvingDialog)
        self.btn_step_back.setObjectName(u"btn_step_back")

        self.horizontalLayout.addWidget(self.btn_step_back)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SolvingDialog)

        QMetaObject.connectSlotsByName(SolvingDialog)
    # setupUi

    def retranslateUi(self, SolvingDialog):
        SolvingDialog.setWindowTitle(QCoreApplication.translate("SolvingDialog", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.btn_step_back.setText(QCoreApplication.translate("SolvingDialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi


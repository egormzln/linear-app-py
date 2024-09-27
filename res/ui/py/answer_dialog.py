# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'answer_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AnswerDialog(object):
    def setupUi(self, AnswerDialog):
        if not AnswerDialog.objectName():
            AnswerDialog.setObjectName(u"AnswerDialog")
        AnswerDialog.resize(228, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AnswerDialog.sizePolicy().hasHeightForWidth())
        AnswerDialog.setSizePolicy(sizePolicy)
        AnswerDialog.setMinimumSize(QSize(228, 150))
        AnswerDialog.setMaximumSize(QSize(228, 228))
        self.verticalLayout_2 = QVBoxLayout(AnswerDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_task_status = QLabel(AnswerDialog)
        self.lbl_task_status.setObjectName(u"lbl_task_status")
        self.lbl_task_status.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_task_status)

        self.lbl_answer = QLabel(AnswerDialog)
        self.lbl_answer.setObjectName(u"lbl_answer")
        self.lbl_answer.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_answer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_answer_ok = QDialogButtonBox(AnswerDialog)
        self.btn_answer_ok.setObjectName(u"btn_answer_ok")
        self.btn_answer_ok.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout.addWidget(self.btn_answer_ok)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(AnswerDialog)

        QMetaObject.connectSlotsByName(AnswerDialog)
    # setupUi

    def retranslateUi(self, AnswerDialog):
        AnswerDialog.setWindowTitle(QCoreApplication.translate("AnswerDialog", u"\u041e\u0442\u0432\u0435\u0442", None))
        self.lbl_task_status.setText(QCoreApplication.translate("AnswerDialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.lbl_answer.setText(QCoreApplication.translate("AnswerDialog", u"\u041e\u0442\u0432\u0435\u0442: 10", None))
    # retranslateUi


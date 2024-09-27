# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instruction_dialog.ui'
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
    QLabel, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_InstructionDialog(object):
    def setupUi(self, InstructionDialog):
        if not InstructionDialog.objectName():
            InstructionDialog.setObjectName(u"InstructionDialog")
        InstructionDialog.resize(608, 382)
        InstructionDialog.setMinimumSize(QSize(608, 382))
        InstructionDialog.setMaximumSize(QSize(608, 382))
        self.verticalLayout_2 = QVBoxLayout(InstructionDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(InstructionDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 565, 504))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_instruction = QLabel(self.scrollAreaWidgetContents)
        self.lbl_instruction.setObjectName(u"lbl_instruction")
        self.lbl_instruction.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lbl_instruction)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.btn_instruction_close = QDialogButtonBox(InstructionDialog)
        self.btn_instruction_close.setObjectName(u"btn_instruction_close")
        self.btn_instruction_close.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.btn_instruction_close)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(InstructionDialog)

        QMetaObject.connectSlotsByName(InstructionDialog)
    # setupUi

    def retranslateUi(self, InstructionDialog):
        InstructionDialog.setWindowTitle(QCoreApplication.translate("InstructionDialog", u"\u0418\u043d\u0442\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.lbl_instruction.setText(QCoreApplication.translate("InstructionDialog", u"\u041e\u0431\u0449\u0438\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f:\n"
"1. \u041f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 \u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f \u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435 \u043e\u0442 1 \u0434\u043e 16.\n"
"2. \u0427\u0438\u0441\u043b\u043e \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439 < \u0447\u0438\u0441\u043b\u0430 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445.\n"
"3. 0\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u043d\u0430 \u0432\u0432\u043e\u0434\u0438\u043c\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435: \u0441 != 0, b >= 0.\n"
"\n"
"\u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0441 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u0439 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0431\u0430\u0437\u043e\u0432\u044b"
                        "\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f \u0437\u0430\u0434\u0430\u0447\u0438:\n"
"1.  \u0427\u0438\u0441\u043b\u043e \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445\n"
"2. \u0427\u0438\u0441\u043b\u043e \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439\n"
"3. \u0422\u0438\u043f \u0437\u0430\u0434\u0430\u0447\u0438 (\u041c\u0438\u043d\u0438\u043c\u0443\u043c / \u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c)\n"
"4. \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0434\u0440\u043e\u0431\u0435\u0439\n"
"5. \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0434\u043e\u0431 \u0440\u0435\u0448\u0435\u043d\u0438\u044f\n"
"6. \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u0414\u0430\u043b\u0435\u0435\"\n"
"7.  \u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u0437\u0430\u0434\u0430\u0447\u0438\n"
"\n"
"\u0414\u0430\u043b\u0435\u0435 \u043f\u0435\u0440\u0435\u0439\u0434"
                        "\u0451\u043c \u043a \u0440\u0435\u0448\u0435\u043d\u0438\u044e\n"
"8. \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u0420\u0435\u0448\u0438\u0442\u044c\"\n"
"9. \u0412 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u043f\u043e\u0441\u043e\u0431\u0430 \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u0432\u044b \u043b\u0438\u0431\u043e \u043f\u0435\u0440\u0435\u0439\u0434\u0451\u0442\u0435 \u0432 \u0438\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c \u043b\u0438\u0431\u043e \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u0435 \u043e\u0442\u0432\u0435\u0442\n"
"\n"
"\u0414\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u0432 \u0438\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u0431\u0438"
                        "\u0440\u0430\u0442\u044c \u043f\u043e\u0434\u0441\u0432\u0435\u0447\u0435\u043d\u043d\u044b\u0435 \u043e\u043f\u043e\u0440\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u0442\u043d\u044b.\n"
"\n"
"\u042d\u0442\u0430\u043f\u044b \u0440\u0435\u0448\u0435\u043d\u0438\u044f:\n"
"1. \u041c\u0435\u0442\u043e\u0434 \u0438\u0441\u043a\u0443\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0431\u0430\u0437\u0438\u0441\u0430 (\u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0437\u0430\u0434\u0430\u043d \u0438\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e)\n"
"2. \u0420\u0435\u0448\u0435\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438 \u0441\u0438\u043c\u043f\u043b\u0435\u043a\u0441-\u043c\u0435\u0442\u043e\u0434\u043e\u043c\n"
"3. \u041e\u0442\u0432\u0435\u0442\n"
"\n"
"\u0415\u0441\u043b\u0438 \u043f\u043e\u043b\u044f \u0431\u0430\u0437\u0438\u0441\u0430 \u043e\u0441\u0442\u0430\u043d\u0443\u0442\u0441\u044f \u043d\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u043c"
                        "\u0438, \u0442\u043e \u0437\u0430\u0434\u0430\u0447\u0430 \u0431\u0443\u0434\u0435\u0442 \u0440\u0435\u0448\u0435\u043d\u0430 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0431\u0430\u0437\u0438\u0441\u0430\n"
"\u041f\u0440\u0438 \u0432\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0431\u0430\u0437\u0438\u0441\u0430 \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u0439\u0434\u0451\u0442 \u0441\u0440\u0430\u0437\u0443 \u043d\u0430 2 \u044d\u0442\u0430\u043f.", None))
    # retranslateUi


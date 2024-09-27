# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_dialog.ui'
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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        if not InfoDialog.objectName():
            InfoDialog.setObjectName(u"InfoDialog")
        InfoDialog.resize(398, 160)
        InfoDialog.setMinimumSize(QSize(398, 160))
        InfoDialog.setMaximumSize(QSize(398, 160))
        InfoDialog.setAcceptDrops(False)
        self.verticalLayout_2 = QVBoxLayout(InfoDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_info = QLabel(InfoDialog)
        self.lbl_info.setObjectName(u"lbl_info")
        self.lbl_info.setScaledContents(False)
        self.lbl_info.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_info)

        self.btn_info_close = QDialogButtonBox(InfoDialog)
        self.btn_info_close.setObjectName(u"btn_info_close")
        self.btn_info_close.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.btn_info_close)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(InfoDialog)

        QMetaObject.connectSlotsByName(InfoDialog)
    # setupUi

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QCoreApplication.translate("InfoDialog", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.lbl_info.setText(QCoreApplication.translate("InfoDialog", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.</p><p>\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a <a href=\"https://t.me/egormzln\"><span style=\" text-decoration: underline; color:#094fd1;\">@egormzln</span></a></p></body></html>", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Formulario(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(430, 227)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.labelTaprendizaje = QLabel(Form)
        self.labelTaprendizaje.setObjectName(u"labelTaprendizaje")
        self.labelTaprendizaje.setGeometry(QRect(30, 50, 181, 16))
        self.labelEpermisible = QLabel(Form)
        self.labelEpermisible.setObjectName(u"labelEpermisible")
        self.labelEpermisible.setGeometry(QRect(240, 50, 151, 16))
        self.lineEditTAprendizaje = QLineEdit(Form)
        self.lineEditTAprendizaje.setObjectName(u"lineEditTAprendizaje")
        self.lineEditTAprendizaje.setGeometry(QRect(30, 80, 181, 31))
        self.lineEditEPermisible = QLineEdit(Form)
        self.lineEditEPermisible.setObjectName(u"lineEditEPermisible")
        self.lineEditEPermisible.setGeometry(QRect(240, 80, 151, 31))
        self.pushButtonEjecutar = QPushButton(Form)
        self.pushButtonEjecutar.setObjectName(u"pushButtonEjecutar")
        self.pushButtonEjecutar.setGeometry(QRect(32, 150, 361, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTaprendizaje.setText(QCoreApplication.translate("Form", u"TAZA DE APRENDIZAJE ", None))
        self.labelEpermisible.setText(QCoreApplication.translate("Form", u"ERROR PERMISIBLE", None))
        self.pushButtonEjecutar.setText(QCoreApplication.translate("Form", u"Ejecutar", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_textflag(object):
    def setupUi(self, textflag):
        textflag.setObjectName("textflag")
        textflag.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(textflag.sizePolicy().hasHeightForWidth())
        textflag.setSizePolicy(sizePolicy)
        self.polosa1 = QtWidgets.QGroupBox(textflag)
        self.polosa1.setGeometry(QtCore.QRect(10, 170, 120, 80))
        self.polosa1.setObjectName("polosa1")
        self.radioButton = QtWidgets.QRadioButton(self.polosa1)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 81, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.polosa1)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 91, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.polosa1)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(textflag)
        self.pushButton.setGeometry(QtCore.QRect(90, 260, 231, 23))
        self.pushButton.setObjectName("pushButton")
        self.polosa1_2 = QtWidgets.QGroupBox(textflag)
        self.polosa1_2.setGeometry(QtCore.QRect(140, 170, 120, 80))
        self.polosa1_2.setObjectName("polosa1_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.polosa1_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 60, 81, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.polosa1_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 40, 91, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.polosa1_2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.polosa1_3 = QtWidgets.QGroupBox(textflag)
        self.polosa1_3.setGeometry(QtCore.QRect(270, 170, 120, 80))
        self.polosa1_3.setObjectName("polosa1_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.polosa1_3)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 60, 81, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.polosa1_3)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 40, 91, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.polosa1_3)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.label = QtWidgets.QLabel(textflag)
        self.label.setGeometry(QtCore.QRect(120, 30, 141, 71))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(textflag)
        QtCore.QMetaObject.connectSlotsByName(textflag)

    def retranslateUi(self, textflag):
        _translate = QtCore.QCoreApplication.translate
        textflag.setWindowTitle(_translate("textflag", "Dialog"))
        self.polosa1.setTitle(_translate("textflag", "Верх"))
        self.radioButton.setText(_translate("textflag", "Красный"))
        self.radioButton_2.setText(_translate("textflag", "Синий"))
        self.radioButton_3.setText(_translate("textflag", "Белый"))
        self.pushButton.setText(_translate("textflag", "Нарисовать"))
        self.polosa1_2.setTitle(_translate("textflag", "Центр"))
        self.radioButton_4.setText(_translate("textflag", "Красный"))
        self.radioButton_5.setText(_translate("textflag", "Синий"))
        self.radioButton_6.setText(_translate("textflag", "Белый"))
        self.polosa1_3.setTitle(_translate("textflag", "Низ"))
        self.radioButton_7.setText(_translate("textflag", "Красный"))
        self.radioButton_8.setText(_translate("textflag", "Синий"))
        self.radioButton_9.setText(_translate("textflag", "Белый"))


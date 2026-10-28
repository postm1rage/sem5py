# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nim(object):
    def setupUi(self, nim):
        nim.setObjectName("nim")
        nim.resize(460, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(nim.sizePolicy().hasHeightForWidth())
        nim.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(nim)
        self.centralwidget.setObjectName("centralwidget")
        self.labelStones = QtWidgets.QLabel(self.centralwidget)
        self.labelStones.setGeometry(QtCore.QRect(20, 20, 180, 25))
        self.labelStones.setObjectName("labelStones")
        self.spinBoxStones = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxStones.setGeometry(QtCore.QRect(200, 20, 100, 25))
        self.spinBoxStones.setMinimum(1)
        self.spinBoxStones.setMaximum(999)
        self.spinBoxStones.setProperty("value", 15)
        self.spinBoxStones.setObjectName("spinBoxStones")
        self.pushButtonNewGame = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNewGame.setGeometry(QtCore.QRect(310, 20, 130, 25))
        self.pushButtonNewGame.setObjectName("pushButtonNewGame")
        self.labelRemaining = QtWidgets.QLabel(self.centralwidget)
        self.labelRemaining.setGeometry(QtCore.QRect(20, 70, 420, 40))
        self.labelRemaining.setObjectName("labelRemaining")
        self.labelStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(20, 120, 420, 25))
        self.labelStatus.setObjectName("labelStatus")
        self.labelMove = QtWidgets.QLabel(self.centralwidget)
        self.labelMove.setGeometry(QtCore.QRect(20, 170, 200, 25))
        self.labelMove.setObjectName("labelMove")
        self.spinBoxMove = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxMove.setGeometry(QtCore.QRect(220, 170, 80, 25))
        self.spinBoxMove.setMinimum(0)
        self.spinBoxMove.setMaximum(3)
        self.spinBoxMove.setProperty("value", 1)
        self.spinBoxMove.setObjectName("spinBoxMove")
        self.pushButtonTake = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTake.setGeometry(QtCore.QRect(310, 170, 130, 25))
        self.pushButtonTake.setObjectName("pushButtonTake")
        self.textEditLog = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditLog.setGeometry(QtCore.QRect(20, 210, 420, 140))
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setObjectName("textEditLog")
        nim.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(nim)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 21))
        self.menubar.setObjectName("menubar")
        nim.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(nim)
        self.statusbar.setObjectName("statusbar")
        nim.setStatusBar(self.statusbar)

        self.retranslateUi(nim)
        QtCore.QMetaObject.connectSlotsByName(nim)

    def retranslateUi(self, nim):
        _translate = QtCore.QCoreApplication.translate
        nim.setWindowTitle(_translate("nim", "Псевдоним"))
        self.labelStones.setText(_translate("nim", "Начальное число камней:"))
        self.pushButtonNewGame.setText(_translate("nim", "Новая игра"))
        self.labelRemaining.setText(_translate("nim", "Камней на столе: —"))
        self.labelRemaining.setStyleSheet(_translate("nim", "font-size: 20px; font-weight: bold;"))
        self.labelStatus.setText(_translate("nim", "Нажмите «Новая игра» для начала"))
        self.labelMove.setText(_translate("nim", "Ваш ход (1–3 камня):"))
        self.pushButtonTake.setText(_translate("nim", "Взять"))


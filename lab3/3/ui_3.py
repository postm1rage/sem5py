# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLeft = QtWidgets.QPushButton(self.centralwidget)
        self.btnLeft.setObjectName("btnLeft")
        self.horizontalLayout.addWidget(self.btnLeft)
        self.btnRight = QtWidgets.QPushButton(self.centralwidget)
        self.btnRight.setObjectName("btnRight")
        self.horizontalLayout.addWidget(self.btnRight)
        self.btnAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnAll.setObjectName("btnAll")
        self.horizontalLayout.addWidget(self.btnAll)
        self.btnR = QtWidgets.QPushButton(self.centralwidget)
        self.btnR.setObjectName("btnR")
        self.horizontalLayout.addWidget(self.btnR)
        self.btnG = QtWidgets.QPushButton(self.centralwidget)
        self.btnG.setObjectName("btnG")
        self.horizontalLayout.addWidget(self.btnG)
        self.btnB = QtWidgets.QPushButton(self.centralwidget)
        self.btnB.setObjectName("btnB")
        self.horizontalLayout.addWidget(self.btnB)
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout.addWidget(self.imageLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактор изображений"))
        self.btnLeft.setText(_translate("MainWindow", "⟲ Влево"))
        self.btnRight.setText(_translate("MainWindow", "⟳ Вправо"))
        self.btnAll.setText(_translate("MainWindow", "Все каналы"))
        self.btnR.setText(_translate("MainWindow", "Только R"))
        self.btnG.setText(_translate("MainWindow", "Только G"))
        self.btnB.setText(_translate("MainWindow", "Только B"))
        self.btnOpen.setText(_translate("MainWindow", "Открыть"))
        self.imageLabel.setText(_translate("MainWindow", "Изображение не загружено"))
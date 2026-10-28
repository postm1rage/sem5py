# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoad = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoad.setObjectName("btnLoad")
        self.horizontalLayout.addWidget(self.btnLoad)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelMax = QtWidgets.QLabel(self.centralwidget)
        self.labelMax.setObjectName("labelMax")
        self.verticalLayout.addWidget(self.labelMax)
        self.labelMin = QtWidgets.QLabel(self.centralwidget)
        self.labelMin.setObjectName("labelMin")
        self.verticalLayout.addWidget(self.labelMin)
        self.labelAvg = QtWidgets.QLabel(self.centralwidget)
        self.labelAvg.setObjectName("labelAvg")
        self.verticalLayout.addWidget(self.labelAvg)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ чисел из файла"))
        self.btnLoad.setText(_translate("MainWindow", "Загрузить"))
        self.btnSave.setText(_translate("MainWindow", "Сохранить"))
        self.labelMax.setText(_translate("MainWindow", "Максимум: —"))
        self.labelMin.setText(_translate("MainWindow", "Минимум: —"))
        self.labelAvg.setText(_translate("MainWindow", "Среднее: —"))
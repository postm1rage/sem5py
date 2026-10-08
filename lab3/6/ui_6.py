# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnColor = QtWidgets.QPushButton(self.centralwidget)
        self.btnColor.setObjectName("btnColor")
        self.horizontalLayout.addWidget(self.btnColor)
        self.labelScale = QtWidgets.QLabel(self.centralwidget)
        self.labelScale.setObjectName("labelScale")
        self.horizontalLayout.addWidget(self.labelScale)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sliderScale = QtWidgets.QSlider(self.centralwidget)
        self.sliderScale.setMinimum(20)
        self.sliderScale.setMaximum(200)
        self.sliderScale.setValue(100)
        self.sliderScale.setOrientation(QtCore.Qt.Horizontal)
        self.sliderScale.setObjectName("sliderScale")
        self.verticalLayout.addWidget(self.sliderScale)
        self.canvasWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvasWidget.sizePolicy().hasHeightForWidth())
        self.canvasWidget.setSizePolicy(sizePolicy)
        self.canvasWidget.setObjectName("canvasWidget")
        self.verticalLayout.addWidget(self.canvasWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Смайлик"))
        self.btnColor.setText(_translate("MainWindow", "Выбрать цвет"))
        self.labelScale.setText(_translate("MainWindow", "Масштаб: 100%"))
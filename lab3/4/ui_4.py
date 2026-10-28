# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4.ui'
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
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.labelValue = QtWidgets.QLabel(self.centralwidget)
        self.labelValue.setObjectName("labelValue")
        self.horizontalLayout.addWidget(self.labelValue)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sliderAlpha = QtWidgets.QSlider(self.centralwidget)
        self.sliderAlpha.setMinimum(0)
        self.sliderAlpha.setMaximum(100)
        self.sliderAlpha.setValue(100)
        self.sliderAlpha.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAlpha.setObjectName("sliderAlpha")
        self.verticalLayout.addWidget(self.sliderAlpha)
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout.addWidget(self.imageLabel)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Регулятор прозрачности"))
        self.btnOpen.setText(_translate("MainWindow", "Открыть изображение"))
        self.labelValue.setText(_translate("MainWindow", "Прозрачность: 100%"))
        self.imageLabel.setText(_translate("MainWindow", "Изображение не загружено"))
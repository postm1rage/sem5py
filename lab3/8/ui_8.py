# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '8.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout.addWidget(self.labelTitle)
        self.labelStep = QtWidgets.QLabel(self.centralwidget)
        self.labelStep.setObjectName("labelStep")
        self.horizontalLayout.addWidget(self.labelStep)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sliderStep = QtWidgets.QSlider(self.centralwidget)
        self.sliderStep.setMinimum(0)
        self.sliderStep.setMaximum(5)
        self.sliderStep.setValue(1)
        self.sliderStep.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStep.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderStep.setTickInterval(1)
        self.sliderStep.setObjectName("sliderStep")
        self.verticalLayout.addWidget(self.sliderStep)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "L-система"))
        self.labelTitle.setText(_translate("MainWindow", "Название: —"))
        self.labelStep.setText(_translate("MainWindow", "Шаг: 1"))
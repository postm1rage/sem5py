# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_antiplag(object):
    def setupUi(self, antiplag):
        antiplag.setObjectName("antiplag")
        antiplag.resize(700, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(antiplag.sizePolicy().hasHeightForWidth())
        antiplag.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(antiplag)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.thresholdLayout = QtWidgets.QHBoxLayout()
        self.thresholdLayout.setObjectName("thresholdLayout")
        self.labelThreshold = QtWidgets.QLabel(self.centralwidget)
        self.labelThreshold.setObjectName("labelThreshold")
        self.thresholdLayout.addWidget(self.labelThreshold)
        self.doubleSpinBoxThreshold = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxThreshold.setMinimum(0.0)
        self.doubleSpinBoxThreshold.setMaximum(100.0)
        self.doubleSpinBoxThreshold.setProperty("value", 50.0)
        self.doubleSpinBoxThreshold.setDecimals(1)
        self.doubleSpinBoxThreshold.setObjectName("doubleSpinBoxThreshold")
        self.thresholdLayout.addWidget(self.doubleSpinBoxThreshold)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.thresholdLayout.addItem(spacerItem)
        self.mainLayout.addLayout(self.thresholdLayout)
        self.textsLayout = QtWidgets.QHBoxLayout()
        self.textsLayout.setObjectName("textsLayout")
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setObjectName("leftLayout")
        self.labelOriginal = QtWidgets.QLabel(self.centralwidget)
        self.labelOriginal.setObjectName("labelOriginal")
        self.leftLayout.addWidget(self.labelOriginal)
        self.plainTextEditOriginal = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditOriginal.setObjectName("plainTextEditOriginal")
        self.leftLayout.addWidget(self.plainTextEditOriginal)
        self.textsLayout.addLayout(self.leftLayout)
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightLayout.setObjectName("rightLayout")
        self.labelChecked = QtWidgets.QLabel(self.centralwidget)
        self.labelChecked.setObjectName("labelChecked")
        self.rightLayout.addWidget(self.labelChecked)
        self.plainTextEditChecked = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditChecked.setObjectName("plainTextEditChecked")
        self.rightLayout.addWidget(self.plainTextEditChecked)
        self.textsLayout.addLayout(self.rightLayout)
        self.mainLayout.addLayout(self.textsLayout)
        self.pushButtonCompare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCompare.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButtonCompare.setObjectName("pushButtonCompare")
        self.mainLayout.addWidget(self.pushButtonCompare)
        antiplag.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(antiplag)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        antiplag.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(antiplag)
        self.statusbar.setObjectName("statusbar")
        antiplag.setStatusBar(self.statusbar)

        self.retranslateUi(antiplag)
        QtCore.QMetaObject.connectSlotsByName(antiplag)

    def retranslateUi(self, antiplag):
        _translate = QtCore.QCoreApplication.translate
        antiplag.setWindowTitle(_translate("antiplag", "Антиплагиат"))
        self.labelThreshold.setText(_translate("antiplag", "Порог срабатывания, %:"))
        self.labelOriginal.setText(_translate("antiplag", "Оригинал:"))
        self.plainTextEditOriginal.setPlaceholderText(_translate("antiplag", "Вставьте сюда эталонный текст"))
        self.labelChecked.setText(_translate("antiplag", "Проверяемый текст:"))
        self.plainTextEditChecked.setPlaceholderText(_translate("antiplag", "Вставьте сюда проверяемый текст"))
        self.pushButtonCompare.setText(_translate("antiplag", "Сравнить"))


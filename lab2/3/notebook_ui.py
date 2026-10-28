# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_notebook(object):
    def setupUi(self, notebook):
        notebook.setObjectName("notebook")
        notebook.resize(480, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(notebook.sizePolicy().hasHeightForWidth())
        notebook.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(notebook)
        self.centralwidget.setObjectName("centralwidget")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(20, 20, 100, 25))
        self.labelName.setObjectName("labelName")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(120, 20, 340, 25))
        self.lineEditName.setObjectName("lineEditName")
        self.labelPhone = QtWidgets.QLabel(self.centralwidget)
        self.labelPhone.setGeometry(QtCore.QRect(20, 60, 100, 25))
        self.labelPhone.setObjectName("labelPhone")
        self.lineEditPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPhone.setGeometry(QtCore.QRect(120, 60, 340, 25))
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(120, 100, 340, 30))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 150, 440, 240))
        self.listWidget.setObjectName("listWidget")
        notebook.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(notebook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        notebook.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(notebook)
        self.statusbar.setObjectName("statusbar")
        notebook.setStatusBar(self.statusbar)

        self.retranslateUi(notebook)
        QtCore.QMetaObject.connectSlotsByName(notebook)

    def retranslateUi(self, notebook):
        _translate = QtCore.QCoreApplication.translate
        notebook.setWindowTitle(_translate("notebook", "Записная книжка"))
        self.labelName.setText(_translate("notebook", "Имя:"))
        self.lineEditName.setPlaceholderText(_translate("notebook", "Введите имя контакта"))
        self.labelPhone.setText(_translate("notebook", "Номер:"))
        self.lineEditPhone.setPlaceholderText(_translate("notebook", "Введите номер телефона"))
        self.pushButtonAdd.setText(_translate("notebook", "Добавить"))


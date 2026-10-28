# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_diary(object):
    def setupUi(self, diary):
        diary.setObjectName("diary")
        diary.resize(560, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(diary.sizePolicy().hasHeightForWidth())
        diary.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(diary)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEvent = QtWidgets.QLabel(self.centralwidget)
        self.labelEvent.setGeometry(QtCore.QRect(20, 20, 100, 25))
        self.labelEvent.setObjectName("labelEvent")
        self.lineEditEvent = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEvent.setGeometry(QtCore.QRect(120, 20, 400, 25))
        self.lineEditEvent.setObjectName("lineEditEvent")
        self.labelDate = QtWidgets.QLabel(self.centralwidget)
        self.labelDate.setGeometry(QtCore.QRect(20, 60, 100, 25))
        self.labelDate.setObjectName("labelDate")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(120, 60, 150, 25))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.labelTime = QtWidgets.QLabel(self.centralwidget)
        self.labelTime.setGeometry(QtCore.QRect(300, 60, 60, 25))
        self.labelTime.setObjectName("labelTime")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(360, 60, 160, 25))
        self.timeEdit.setObjectName("timeEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(120, 100, 400, 30))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 150, 500, 240))
        self.listWidget.setObjectName("listWidget")
        diary.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(diary)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        diary.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(diary)
        self.statusbar.setObjectName("statusbar")
        diary.setStatusBar(self.statusbar)

        self.retranslateUi(diary)
        QtCore.QMetaObject.connectSlotsByName(diary)

    def retranslateUi(self, diary):
        _translate = QtCore.QCoreApplication.translate
        diary.setWindowTitle(_translate("diary", "Ежедневник"))
        self.labelEvent.setText(_translate("diary", "Событие:"))
        self.lineEditEvent.setPlaceholderText(_translate("diary", "Введите название события"))
        self.labelDate.setText(_translate("diary", "Дата:"))
        self.dateEdit.setDisplayFormat(_translate("diary", "dd.MM.yyyy"))
        self.labelTime.setText(_translate("diary", "Время:"))
        self.timeEdit.setDisplayFormat(_translate("diary", "HH:mm"))
        self.pushButtonAdd.setText(_translate("diary", "Добавить"))


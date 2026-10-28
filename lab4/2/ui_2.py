# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(920, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.rootLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.rootLayout.setObjectName('rootLayout')
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName('buttonLayout')
        self.openDbButton = QtWidgets.QPushButton(self.centralwidget)
        self.openDbButton.setObjectName('openDbButton')
        self.buttonLayout.addWidget(self.openDbButton)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName('addButton')
        self.buttonLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setObjectName('editButton')
        self.buttonLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName('deleteButton')
        self.buttonLayout.addWidget(self.deleteButton)
        self.rootLayout.addLayout(self.buttonLayout)
        self.databaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.databaseLabel.setObjectName('databaseLabel')
        self.rootLayout.addWidget(self.databaseLabel)
        self.filmsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.filmsTable.setObjectName('filmsTable')
        self.rootLayout.addWidget(self.filmsTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", 'Каталог фильмов'))
        self.openDbButton.setText(_translate("MainWindow", 'Открыть базу SQLite'))
        self.addButton.setText(_translate("MainWindow", 'Добавить'))
        self.editButton.setText(_translate("MainWindow", 'Изменить'))
        self.deleteButton.setText(_translate("MainWindow", 'Удалить'))
        self.databaseLabel.setText(_translate("MainWindow", 'Текущая база данных'))

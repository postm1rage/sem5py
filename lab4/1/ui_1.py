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
        self.filterLayout = QtWidgets.QHBoxLayout()
        self.filterLayout.setObjectName('filterLayout')
        self.schoolCaption = QtWidgets.QLabel(self.centralwidget)
        self.schoolCaption.setObjectName('schoolCaption')
        self.filterLayout.addWidget(self.schoolCaption)
        self.schoolCombo = QtWidgets.QComboBox(self.centralwidget)
        self.schoolCombo.setObjectName('schoolCombo')
        self.filterLayout.addWidget(self.schoolCombo)
        self.classCaption = QtWidgets.QLabel(self.centralwidget)
        self.classCaption.setObjectName('classCaption')
        self.filterLayout.addWidget(self.classCaption)
        self.classCombo = QtWidgets.QComboBox(self.centralwidget)
        self.classCombo.setObjectName('classCombo')
        self.filterLayout.addWidget(self.classCombo)
        self.openCsvButton = QtWidgets.QPushButton(self.centralwidget)
        self.openCsvButton.setObjectName('openCsvButton')
        self.filterLayout.addWidget(self.openCsvButton)
        self.rootLayout.addLayout(self.filterLayout)
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setObjectName('fileLabel')
        self.rootLayout.addWidget(self.fileLabel)
        self.resultsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.resultsTable.setObjectName('resultsTable')
        self.rootLayout.addWidget(self.resultsTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", 'Результаты олимпиады'))
        self.schoolCaption.setText(_translate("MainWindow", 'Школа:'))
        self.classCaption.setText(_translate("MainWindow", 'Класс:'))
        self.openCsvButton.setText(_translate("MainWindow", 'Открыть CSV'))
        self.fileLabel.setText(_translate("MainWindow", 'Выберите CSV-файл с результатами олимпиады'))

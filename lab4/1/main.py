import csv
import io
import sys
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_1 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.people = []
        self.ui.resultsTable.setColumnCount(3)
        self.ui.resultsTable.setHorizontalHeaderLabels(['Логин', 'ФИО', 'Суммарный балл'])
        self.ui.resultsTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.resultsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.resultsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.openCsvButton.clicked.connect(self.open_csv)
        self.ui.schoolCombo.currentIndexChanged.connect(self.show_people)
        self.ui.classCombo.currentIndexChanged.connect(self.show_people)
        self.ui.schoolCombo.addItem('Все школы', '')
        self.ui.classCombo.addItem('Все классы', '')

    def open_csv(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите результаты олимпиады', str(Path.home()), 'CSV (*.csv);;Все файлы (*)')
        if not path:
            return
        data = Path(path).read_bytes()
        try:
            text = data.decode('utf-8-sig')
        except UnicodeDecodeError:
            text = data.decode('cp1251')
        rows = csv.DictReader(io.StringIO(text))
        people = []
        for row in rows:
            login = row['login'].strip()
            parts = login.split('-')
            people.append((login, row['user_name'].strip(), int(row['Score']), parts[-3], parts[-2]))
        self.people = people
        self.ui.schoolCombo.blockSignals(True)
        self.ui.classCombo.blockSignals(True)
        self.ui.schoolCombo.clear()
        self.ui.classCombo.clear()
        self.ui.schoolCombo.addItem('Все школы', '')
        self.ui.classCombo.addItem('Все классы', '')
        for school in sorted({p[3] for p in people}, key=lambda x: int(x)):
            self.ui.schoolCombo.addItem(school, school)
        for grade in sorted({p[4] for p in people}, key=lambda x: int(x)):
            self.ui.classCombo.addItem(grade, grade)
        self.ui.schoolCombo.blockSignals(False)
        self.ui.classCombo.blockSignals(False)
        self.ui.fileLabel.setText(Path(path).name)
        self.show_people()

    def show_people(self):
        school = self.ui.schoolCombo.currentData()
        grade = self.ui.classCombo.currentData()
        people = [p for p in self.people if (not school or p[3] == school) and (not grade or p[4] == grade)]
        scores = sorted((p[2] for p in people), reverse=True)
        colors = {1: QtGui.QColor('#ffe59b'), 2: QtGui.QColor('#dce3ec'), 3: QtGui.QColor('#e9b994')}
        table = self.ui.resultsTable
        table.setRowCount(len(people))
        for i, (login, name, score, _, _) in enumerate(people):
            rank = 1 + scores.index(score)
            for j, value in enumerate((login, name, str(score))):
                item = QtWidgets.QTableWidgetItem(value)
                if rank in colors:
                    item.setBackground(colors[rank])
                table.setItem(i, j, item)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

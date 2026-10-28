import sqlite3
import sys
from datetime import date
from pathlib import Path
from PyQt5 import QtCore, QtWidgets
from ui_2 import Ui_MainWindow


class FilmDialog(QtWidgets.QDialog):
    def __init__(self, columns, genres, values=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Изменить фильм' if values else 'Добавить фильм')
        self.fields = {}
        layout = QtWidgets.QVBoxLayout(self)
        form = QtWidgets.QFormLayout()
        for column in columns:
            name, field_type, is_pk = column
            if name.lower() == 'genre' and genres:
                field = QtWidgets.QComboBox()
                for genre_id, title in genres:
                    field.addItem(str(title), genre_id)
                if values:
                    index = field.findData(values[name])
                    if index >= 0:
                        field.setCurrentIndex(index)
            else:
                field = QtWidgets.QLineEdit()
                if values and values[name] is not None:
                    field.setText(str(values[name]))
                if is_pk:
                    field.setReadOnly(True)
                    if not values:
                        field.setPlaceholderText('Автоматически')
            form.addRow(name, field)
            self.fields[name] = field
        layout.addLayout(form)
        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.columns = columns

    def values(self):
        result = {}
        for name, field_type, is_pk in self.columns:
            if is_pk:
                continue
            field = self.fields[name]
            value = field.currentData() if isinstance(field, QtWidgets.QComboBox) else field.text().strip()
            if name.lower() in ('year', 'duration'):
                try:
                    value = int(value)
                except ValueError:
                    raise ValueError(f'Поле {name} должно содержать целое число')
            if name.lower() == 'year' and (value <= 0 or value > date.today().year):
                raise ValueError('Год выпуска должен быть положительным и не больше текущего')
            if name.lower() == 'duration' and value <= 0:
                raise ValueError('Продолжительность должна быть положительной')
            if name.lower() == 'title' and not value:
                raise ValueError('Введите название фильма')
            if field_type.upper().startswith('INT') and name.lower() not in ('year', 'duration'):
                value = int(value)
            result[name] = value
        return result


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        base = Path(QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.AppDataLocation))
        base.mkdir(parents=True, exist_ok=True)
        self.path = base / 'films_db.sqlite'
        self.conn = None
        self.columns = []
        self.genres = []
        self.ui.filmsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.filmsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.filmsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.filmsTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.openDbButton.clicked.connect(self.open_database)
        self.ui.addButton.clicked.connect(self.add_film)
        self.ui.editButton.clicked.connect(self.edit_film)
        self.ui.deleteButton.clicked.connect(self.delete_film)
        self.connect_database(self.path)

    def connect_database(self, path):
        if self.conn:
            self.conn.close()
        self.path = Path(path)
        self.conn = sqlite3.connect(str(self.path))
        self.conn.row_factory = sqlite3.Row
        if not self.conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND lower(name)='films'").fetchone():
            self.conn.executescript('CREATE TABLE Films (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, year INTEGER NOT NULL, genre INTEGER, duration INTEGER NOT NULL); CREATE TABLE genres (id INTEGER PRIMARY KEY, title TEXT NOT NULL);')
            self.conn.executemany('INSERT INTO genres (id, title) VALUES (?, ?)', list(enumerate(['Комедия', 'Драма', 'Боевик', 'Фантастика', 'Мультфильм', 'Триллер', 'Документальный'], 1)))
            self.conn.commit()
        info = self.conn.execute('PRAGMA table_info(Films)').fetchall()
        self.columns = [(row['name'], row['type'], bool(row['pk'])) for row in info]
        self.genres = []
        table = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND lower(name)='genres'").fetchone()
        if table:
            self.genres = [tuple(row) for row in self.conn.execute('SELECT id, title FROM genres ORDER BY title')]
        self.ui.databaseLabel.setText(str(self.path))
        self.refresh()

    def open_database(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть films_db.sqlite', str(Path.home()), 'SQLite (*.sqlite *.db);;Все файлы (*)')
        if path:
            self.connect_database(path)

    def refresh(self):
        cols = [name for name, _, _ in self.columns]
        if any(name.lower() == 'genre' for name in cols) and self.genres:
            parts = [f'COALESCE(g.title, CAST(f."{name}" AS TEXT)) AS "{name}"' if name.lower() == 'genre' else f'f."{name}"' for name in cols]
            query = 'SELECT ' + ', '.join(parts) + ' FROM Films f LEFT JOIN genres g ON f.genre = g.id'
        else:
            query = 'SELECT * FROM Films'
        cursor = self.conn.execute(query)
        headers = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        table = self.ui.filmsTable
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                table.setItem(i, j, QtWidgets.QTableWidgetItem('' if value is None else str(value)))
        table.resizeRowsToContents()

    def selected_record(self):
        row = self.ui.filmsTable.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите фильм в таблице')
            return None
        pk = next(name for name, _, is_pk in self.columns if is_pk)
        first = self.ui.filmsTable.item(row, next(i for i, c in enumerate(self.columns) if c[0] == pk))
        return self.conn.execute(f'SELECT * FROM Films WHERE "{pk}" = ?', (first.text(),)).fetchone()

    def film_form(self, record=None):
        dialog = FilmDialog(self.columns, self.genres, record, self)
        while dialog.exec_() == QtWidgets.QDialog.Accepted:
            try:
                data = dialog.values()
                cols = list(data)
                if record is None:
                    self.conn.execute(f'INSERT INTO Films ({", ".join(chr(34)+c+chr(34) for c in cols)}) VALUES ({", ".join("?" for _ in cols)})', list(data.values()))
                else:
                    pk = next(name for name, _, is_pk in self.columns if is_pk)
                    self.conn.execute(f'UPDATE Films SET {", ".join(chr(34)+c+chr(34)+" = ?" for c in cols)} WHERE "{pk}" = ?', [*data.values(), record[pk]])
                self.conn.commit()
                self.refresh()
                return
            except (ValueError, sqlite3.Error) as error:
                QtWidgets.QMessageBox.warning(dialog, 'Ошибка ввода', str(error))

    def add_film(self):
        self.film_form()

    def edit_film(self):
        record = self.selected_record()
        if record:
            self.film_form(record)

    def delete_film(self):
        record = self.selected_record()
        if record:
            pk = next(name for name, _, is_pk in self.columns if is_pk)
            self.conn.execute(f'DELETE FROM Films WHERE "{pk}" = ?', (record[pk],))
            self.conn.commit()
            self.refresh()

    def closeEvent(self, event):
        if self.conn:
            self.conn.close()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Lab4Films')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

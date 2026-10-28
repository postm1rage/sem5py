import hashlib
import hmac
import os
import sqlite3
import sys
from datetime import date
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_6 import Ui_MainWindow


class Database:
    def __init__(self):
        path = Path(__file__).resolve().with_name('library.sqlite')
        first_run = not path.exists()
        self.connection = sqlite3.connect(str(path))
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL UNIQUE,
                salt TEXT NOT NULL,
                password_hash TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL,
                genre TEXT NOT NULL,
                image BLOB
            );
        ''')
        if first_run:
            self.connection.executemany('INSERT INTO books (title, author, year, genre, image) VALUES (?, ?, ?, ?, NULL)', [
                ('Евгений Онегин', 'Александр Пушкин', 1833, 'Роман в стихах'),
                ('Преступление и наказание', 'Фёдор Достоевский', 1866, 'Роман'),
                ('Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея'),
                ('Мастер и Маргарита', 'Михаил Булгаков', 1966, 'Роман'),
                ('Алые паруса', 'Александр Грин', 1923, 'Повесть'),
            ])
            salt = os.urandom(16)
            hashed = hashlib.pbkdf2_hmac('sha256', b'demo123', salt, 250000)
            self.connection.execute('INSERT INTO users (login, salt, password_hash) VALUES (?, ?, ?)', ('demo', salt.hex(), hashed.hex()))
        self.connection.commit()

    def register(self, login, password):
        salt = os.urandom(16)
        hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 250000)
        self.connection.execute('INSERT INTO users (login, salt, password_hash) VALUES (?, ?, ?)', (login, salt.hex(), hashed.hex()))
        self.connection.commit()

    def verify(self, login, password):
        user = self.connection.execute('SELECT salt, password_hash FROM users WHERE login = ?', (login,)).fetchone()
        if not user:
            return False
        hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bytes.fromhex(user['salt']), 250000)
        return hmac.compare_digest(hashed, bytes.fromhex(user['password_hash']))


class BookDialog(QtWidgets.QDialog):
    def __init__(self, book=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Изменить книгу' if book else 'Добавить книгу')
        self.image = book['image'] if book else None
        layout = QtWidgets.QVBoxLayout(self)
        form = QtWidgets.QFormLayout()
        self.titleEdit = QtWidgets.QLineEdit(book['title'] if book else '')
        self.authorEdit = QtWidgets.QLineEdit(book['author'] if book else '')
        self.yearEdit = QtWidgets.QSpinBox()
        self.yearEdit.setRange(1, date.today().year)
        self.yearEdit.setValue(book['year'] if book else date.today().year)
        self.genreEdit = QtWidgets.QLineEdit(book['genre'] if book else '')
        self.coverButton = QtWidgets.QPushButton('Выбрать изображение')
        self.coverButton.clicked.connect(self.choose_image)
        form.addRow('Название', self.titleEdit)
        form.addRow('Автор', self.authorEdit)
        form.addRow('Год издания', self.yearEdit)
        form.addRow('Жанр', self.genreEdit)
        form.addRow('Изображение', self.coverButton)
        layout.addLayout(form)
        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.validate)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def choose_image(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите обложку', str(Path.home()), 'Изображения (*.png *.jpg *.jpeg *.bmp *.webp)')
        if path:
            self.image = Path(path).read_bytes()
            self.coverButton.setText(Path(path).name)

    def validate(self):
        if not all((self.titleEdit.text().strip(), self.authorEdit.text().strip(), self.genreEdit.text().strip())):
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Заполните название, автора и жанр')
            return
        self.accept()

    def values(self):
        return (self.titleEdit.text().strip(), self.authorEdit.text().strip(), self.yearEdit.value(), self.genreEdit.text().strip(), self.image)


class LibraryWindow(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pages.setCurrentWidget(self.ui.catalogPage)
        self.rows = []
        self.ui.booksTable.setColumnCount(4)
        self.ui.booksTable.setHorizontalHeaderLabels(['Название', 'Автор', 'Год', 'Жанр'])
        self.ui.booksTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.booksTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.booksTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.booksTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.booksTable.itemSelectionChanged.connect(self.show_selected_book)
        self.ui.authorSearch.textChanged.connect(self.refresh)
        self.ui.titleSearch.textChanged.connect(self.refresh)
        self.ui.addBookButton.clicked.connect(self.add_book)
        self.ui.editBookButton.clicked.connect(self.edit_book)
        self.ui.deleteBookButton.clicked.connect(self.delete_book)
        self.ui.bookInformation.setWordWrap(True)
        self.ui.bookPanel.setFixedWidth(290)
        self.refresh()

    def refresh(self):
        author = '%' + self.ui.authorSearch.text() + '%'
        title = '%' + self.ui.titleSearch.text() + '%'
        self.rows = self.db.connection.execute('SELECT * FROM books WHERE author LIKE ? AND title LIKE ? ORDER BY id DESC', (author, title)).fetchall()
        table = self.ui.booksTable
        table.setRowCount(len(self.rows))
        for index, book in enumerate(self.rows):
            for column, value in enumerate((book['title'], book['author'], book['year'], book['genre'])):
                table.setItem(index, column, QtWidgets.QTableWidgetItem(str(value)))
        if self.rows:
            table.selectRow(0)
        else:
            self.ui.bookImage.clear()
            self.ui.bookInformation.setText('Выберите книгу')

    def selected_book(self):
        row = self.ui.booksTable.currentRow()
        if row < 0 or row >= len(self.rows):
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите книгу в таблице')
            return None
        return self.rows[row]

    def empty_cover(self):
        pixmap = QtGui.QPixmap(210, 255)
        pixmap.fill(QtGui.QColor('#e9edf3'))
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtGui.QColor('#607993'), 3))
        painter.setBrush(QtGui.QColor('#c7d8e8'))
        painter.drawRoundedRect(35, 30, 140, 160, 9, 9)
        painter.drawLine(56, 58, 150, 58)
        painter.drawLine(56, 78, 140, 78)
        painter.setPen(QtGui.QColor('#506577'))
        painter.drawText(QtCore.QRect(0, 200, 210, 45), QtCore.Qt.AlignCenter, 'Нет обложки')
        painter.end()
        return pixmap

    def show_selected_book(self):
        row = self.ui.booksTable.currentRow()
        if row < 0 or row >= len(self.rows):
            return
        book = self.rows[row]
        if book['image']:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(book['image'])
            if pixmap.isNull():
                pixmap = self.empty_cover()
        else:
            pixmap = self.empty_cover()
        self.ui.bookImage.setPixmap(pixmap.scaled(240, 260, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.bookInformation.setText(f"Название: {book['title']}\nАвтор: {book['author']}\nГод: {book['year']}\nЖанр: {book['genre']}")

    def add_book(self):
        dialog = BookDialog(parent=self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.db.connection.execute('INSERT INTO books (title, author, year, genre, image) VALUES (?, ?, ?, ?, ?)', dialog.values())
            self.db.connection.commit()
            self.refresh()

    def edit_book(self):
        book = self.selected_book()
        if book:
            dialog = BookDialog(book, self)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.db.connection.execute('UPDATE books SET title = ?, author = ?, year = ?, genre = ?, image = ? WHERE id = ?', (*dialog.values(), book['id']))
                self.db.connection.commit()
                self.refresh()

    def delete_book(self):
        book = self.selected_book()
        if book:
            self.db.connection.execute('DELETE FROM books WHERE id = ?', (book['id'],))
            self.db.connection.commit()
            self.refresh()


class AuthWindow(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pages.setCurrentWidget(self.ui.authPage)
        self.ui.authPage.setMaximumWidth(480)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registrationButton.clicked.connect(self.register)
        self.ui.passwordEdit.returnPressed.connect(self.login)
        self.library = None

    def credentials(self):
        return self.ui.usernameEdit.text().strip(), self.ui.passwordEdit.text()

    def register(self):
        login, password = self.credentials()
        if not login or not password:
            self.ui.authStatus.setText('Введите логин и пароль')
            return
        try:
            self.db.register(login, password)
        except sqlite3.IntegrityError:
            self.ui.authStatus.setText('Этот логин уже занят')
        else:
            self.ui.authStatus.setText('Регистрация выполнена. Теперь войдите.')

    def login(self):
        login, password = self.credentials()
        if self.db.verify(login, password):
            self.library = LibraryWindow(self.db)
            self.library.show()
            self.close()
        else:
            self.ui.authStatus.setText('Неверный логин или пароль')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Lab4Library')
    database = Database()
    window = AuthWindow(database)
    window.show()
    sys.exit(app.exec_())

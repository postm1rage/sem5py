import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from notebook_ui import Ui_notebook


class NotebookWindow(QMainWindow, Ui_notebook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Запрет изменения размера окна
        self.setFixedSize(self.size())

        # Кнопка "Добавить"
        self.pushButtonAdd.clicked.connect(self.add_contact)

    def add_contact(self):
        name = self.lineEditName.text().strip()
        phone = self.lineEditPhone.text().strip()

        # Проверка: оба поля обязательны
        if not name or not phone:
            QMessageBox.warning(
                self,
                "Внимание",
                "Заполните и имя, и номер телефона!"
            )
            return

        for numbers in '0123456789':
            if phone not in numbers:
                QMessageBox.warning(
                    self,
                    "Внимание",
                    "Номер должен состоять из цифр!"
                )
                return

        # Добавляем строку в список
        self.listWidget.addItem(f"{name} — {phone}")

        # Очищаем поля и возвращаем фокус на имя
        self.lineEditName.clear()
        self.lineEditPhone.clear()
        self.lineEditName.setFocus()


def main():
    app = QApplication(sys.argv)
    window = NotebookWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
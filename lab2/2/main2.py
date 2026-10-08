import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QDateTime

from diary_ui import Ui_diary


class DiaryWindow(QMainWindow, Ui_diary):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Запрет изменения размера окна
        self.setFixedSize(self.size())

        # Внутренний список событий: [(QDateTime, str), ...]
        self.events = []

        # Начальные значения — текущая дата и время
        now = QDateTime.currentDateTime()
        self.dateEdit.setDate(now.date())
        self.timeEdit.setTime(now.time())

        # Кнопка "Добавить"
        self.pushButtonAdd.clicked.connect(self.add_event)

    def add_event(self):
        text = self.lineEditEvent.text().strip()
        if not text:
            QMessageBox.warning(self, "Внимание", "Введите название события!")
            return

        dt = QDateTime(self.dateEdit.date(), self.timeEdit.time())

        # Добавляем и сортируем по возрастанию даты/времени
        self.events.append((dt, text))
        self.events.sort(key=lambda item: item[0])

        self.refresh_list()

        # Готовим поле для следующего ввода
        self.lineEditEvent.clear()
        self.lineEditEvent.setFocus()

    def refresh_list(self):
        self.listWidget.clear()
        for dt, text in self.events:
            self.listWidget.addItem(dt.toString("dd.MM.yyyy HH:mm") + " — " + text)


def main():
    app = QApplication(sys.argv)
    window = DiaryWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
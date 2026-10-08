import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QColor

from antiplag_ui import Ui_antiplag


# ---------- Алгоритмы сравнения ----------

def normalize(text):
    """Нижний регистр, только буквы/цифры/пробелы, разбивка на слова."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    return text.split()


def word_match_percent(original, checked):
    """Доля слов проверяемого текста, которые есть в оригинале."""
    orig_words = set(normalize(original))
    checked_words = normalize(checked)
    if not checked_words:
        return 0.0
    matches = sum(1 for w in checked_words if w in orig_words)
    return matches / len(checked_words) * 100.0


def shingle_match_percent(original, checked, n=3):
    """Доля троек подряд идущих слов, совпавших с оригиналом."""
    def shingles(words):
        return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]

    orig_set = set(shingles(normalize(original)))
    checked_list = shingles(normalize(checked))
    if not checked_list:
        return 0.0
    matches = sum(1 for s in checked_list if s in orig_set)
    return matches / len(checked_list) * 100.0


def final_percent(original, checked):
    """Итоговый процент — максимум из двух методов."""
    w = word_match_percent(original, checked)
    s = shingle_match_percent(original, checked, n=3)
    # если текст короче 3 слов — шинглов нет, берём только слова
    if s == 0 and len(normalize(checked)) < 3:
        return w
    return max(w, s)


# ---------- Окно ----------

class AntiplagWindow(QMainWindow, Ui_antiplag):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Запрет изменения размера окна
        self.setFixedSize(self.size())

        # Обработчик кнопки
        self.pushButtonCompare.clicked.connect(self.compare_texts)

        # Начальное сообщение в статусбаре
        self.set_status("Введите тексты и нажмите «Сравнить»", QColor("black"))

    # ---------- Логика ----------

    def compare_texts(self):
        original = self.plainTextEditOriginal.toPlainText()
        checked = self.plainTextEditChecked.toPlainText()

        # Проверка пустых полей
        if not original.strip() or not checked.strip():
            QMessageBox.warning(
                self, "Внимание",
                "Оба текста должны быть заполнены!"
            )
            self.set_status("Заполните оба текста", QColor("darkorange"))
            return

        # Считаем оба показателя
        w = word_match_percent(original, checked)
        s = shingle_match_percent(original, checked, n=3)
        percent = final_percent(original, checked)

        threshold = self.doubleSpinBoxThreshold.value()
        is_plagiat = percent >= threshold

        verdict = "ПЛАГИАТ" if is_plagiat else "УНИКАЛЬНО"
        text = (
            f"{verdict}: совпадение {percent:.1f}% "
            f"(слова {w:.1f}%, фрагменты {s:.1f}%, "
            f"порог {threshold:.1f}%)"
        )

        # Красный — плагиат, зелёный — уникально
        color = QColor("red") if is_plagiat else QColor("green")
        self.set_status(text, color)

    # ---------- Вспомогательное ----------

    def set_status(self, text, color):
        """Пишет текст в статусбар и красит его в нужный цвет."""
        bar = self.statusbar
        bar.setStyleSheet(f"color: {color.name()}; font-weight: bold;")
        bar.showMessage(text)


def main():
    app = QApplication(sys.argv)
    window = AntiplagWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from textflag_ui import Ui_textflag


class FlagWindow(QMainWindow, Ui_textflag):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(self.size())

        self.groups = {}

        self._setup_group("top", {
            self.radioButton:   "Красный",
            self.radioButton_2: "Синий",
            self.radioButton_3: "Белый",
        })
        self._setup_group("middle", {
            self.radioButton_4: "Красный",
            self.radioButton_5: "Синий",
            self.radioButton_6: "Белый",
        })
        self._setup_group("bottom", {
            self.radioButton_7: "Красный",
            self.radioButton_8: "Синий",
            self.radioButton_9: "Белый",
        })

        self.strip_names = {
            "top":    "Верх",
            "middle": "Центр",
            "bottom": "Низ",
        }

        self.pushButton.clicked.connect(self.draw_flag)

    def _setup_group(self, key, mapping):
        group = QButtonGroup(self)
        for radio in mapping:
            group.addButton(radio)
        self.groups[key] = (group, mapping)

    def _get_selected_color(self, key):
        group, mapping = self.groups[key]
        checked = group.checkedButton()
        if checked is None:
            return None
        return mapping[checked]

    def draw_flag(self):
        colors = []
        for key in ("top", "middle", "bottom"):
            color = self._get_selected_color(key)
            if color is None:
                QMessageBox.warning(
                    self,
                    "Внимание",
                    f"Выберите цвет для полосы «{self.strip_names[key]}»!"
                )
                return
            colors.append(color)

        self.label.setText(", ".join(colors))


def main():
    app = QApplication(sys.argv)
    window = FlagWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
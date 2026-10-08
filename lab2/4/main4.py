import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from nim_ui import Ui_nim


MAX_TAKE = 3   # максимум камней за ход


class NimWindow(QMainWindow, Ui_nim):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Запрет изменения размера окна
        self.setFixedSize(self.size())

        self.stones = 0
        self.game_over = True

        self.pushButtonNewGame.clicked.connect(self.start_new_game)
        self.pushButtonTake.clicked.connect(self.player_move)

        self.update_display()

    # ---------- Управление игрой ----------

    def start_new_game(self):
        self.stones = self.spinBoxStones.value()
        self.game_over = False
        self.textEditLog.clear()

        self.log(f"Новая игра. Камней на столе: {self.stones}")
        self.labelStatus.setText("Ваш ход. Возьмите 1–3 камня.")
        self.update_display()

    def player_move(self):
        if self.game_over:
            QMessageBox.information(
                self, "Игра не начата",
                "Нажмите «Новая игра», чтобы начать."
            )
            return

        take = self.spinBoxMove.value()

        # Проверка корректности хода
        if take < 1 or take > MAX_TAKE:
            QMessageBox.warning(
                self, "Неверный ход",
                f"Можно взять от 1 до {MAX_TAKE} камней."
            )
            return

        if take > self.stones:
            QMessageBox.warning(
                self, "Неверный ход",
                f"На столе только {self.stones} камней. "
                f"Нельзя взять больше, чем есть."
            )
            return

        # Ход игрока
        self.stones -= take
        self.log(f"Вы взяли {take}. Осталось: {self.stones}")
        self.update_display()

        # Проверка на победу игрока
        if self.stones == 0:
            self.finish_game("Поздравляем! Вы выиграли!")
            return

        # Ход компьютера
        self.computer_move()

    def computer_move(self):
        take = self.computer_choose_move()
        self.stones -= take
        self.log(f"Компьютер взял {take}. Осталось: {self.stones}")
        self.update_display()

        if self.stones == 0:
            self.finish_game("Компьютер выиграл. Попробуйте ещё раз!")

    def computer_choose_move(self):
        """
        Стратегия ИИ:
        - Проигрышные позиции для того, чей ход: 0, 4, 8, 12, …
        - Если остаток НЕ кратен 4, берём remainder = stones % 4,
          оставляя сопернику кратное 4 (проигрышную позицию).
        - Если остаток кратен 4 — мы в проигрышной позиции,
          берём 1 (любой) и ждём ошибки человека.
        """
        remainder = self.stones % (MAX_TAKE + 1)   # % 4
        if remainder != 0:
            return remainder
        return 1  # проигрышная позиция — ходим «наугад»

    # ---------- Вспомогательное ----------

    def update_display(self):
        self.labelRemaining.setText(f"Камней на столе: {self.stones}")

    def log(self, text):
        self.textEditLog.append(text)

    def finish_game(self, message):
        self.game_over = True
        self.labelStatus.setText(message)
        QMessageBox.information(self, "Игра окончена", message)


def main():
    app = QApplication(sys.argv)
    window = NimWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
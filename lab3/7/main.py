# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl

import ui_7


class PianoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_7.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.notes = [
            ("C4", "Do"), ("C#4", "Do#"), ("D4", "Re"), ("D#4", "Re#"),
            ("E4", "Mi"), ("F4", "Fa"), ("F#4", "Fa#"), ("G4", "Sol"),
            ("G#4", "Sol#"), ("A4", "La"), ("A#4", "La#"), ("B4", "Si")
        ]
        
        self.sounds = {}
        self.load_sounds()
        self.create_buttons()
    
    def load_sounds(self):
        sounds_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "sounds")
        
        for note_name, _ in self.notes:
            sound_path = os.path.join(sounds_dir, "{}.wav".format(note_name))
            
            if os.path.exists(sound_path):
                effect = QSoundEffect(self)
                effect.setSource(QUrl.fromLocalFile(sound_path))
                effect.setVolume(0.8)
                self.sounds[note_name] = effect
            else:
                print("Файл не найден: {}".format(sound_path))
    
    def create_buttons(self):
        layout = QtWidgets.QHBoxLayout(self.ui.keyboardWidget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)
        
        for note_name, note_label in self.notes:
            button = QtWidgets.QPushButton(note_label)
            button.setFixedSize(55, 250)
            
            font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
            button.setFont(font)
            
            if "#" in note_name:
                button.setStyleSheet(
                    "QPushButton { background-color: #333; color: white; border: 1px solid #000; }"
                    "QPushButton:pressed { background-color: #555; }"
                )
            else:
                button.setStyleSheet(
                    "QPushButton { background-color: white; color: black; border: 1px solid #000; }"
                    "QPushButton:pressed { background-color: #ddd; }"
                )
            
            button.clicked.connect(lambda checked, n=note_name: self.play_note(n))
            layout.addWidget(button)
    
    def play_note(self, note_name):
        effect = self.sounds.get(note_name)
        if effect:
            effect.play()
            self.ui.labelInfo.setText("Играет нота: {}".format(note_name))
        else:
            self.ui.labelInfo.setText("Звук для {} не загружен".format(note_name))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PianoWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        loadUi(r"C:\Python\FileOrganizerApplication\ui\interface.ui", self)
        self.setWindowTitle("FileOrganizer")

        self.frame_4.setStyleSheet("QWidget { border: 1px solid black; }")
        self.frame_2.setStyleSheet("QWidget { border: 1px solid black; }")
        self.frame_3.setStyleSheet("QWidget { border: 1px solid black; }")
        self.frame_5.setStyleSheet("QWidget { border: 1px solid black; }")
        self.frame_6.setStyleSheet("QWidget { border: 1px solid black; }")

        # Set background colors for each frame
        self.frame_4.setStyleSheet("background-color: grey;")
        self.frame_2.setStyleSheet("background-color: grey;")
        self.frame_3.setStyleSheet("background-color: grey;")
        self.frame_5.setStyleSheet("background-color: grey;")
        self.frame_6.setStyleSheet("background-color: grey;")


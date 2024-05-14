from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        loadUi(r"C:\Python\FileOrganizerApplication\ui\interface.ui", self)
        self.setWindowTitle("FileOrganizer")

        # Apply styles to the frames
        self.setFrameStyles()

    def setFrameStyles(self):
        # Apply style sheet to each frame to add rounded corners
        self.applyRoundedCorners(self.frame_4)
        self.applyRoundedCorners(self.frame_2)
        self.applyRoundedCorners(self.frame_3)
        self.applyRoundedCorners(self.frame_5)
        self.applyRoundedCorners(self.frame_6)

    def applyRoundedCorners(self, frame):
        # Apply style sheet to add rounded corners to the frame
        frame.setStyleSheet("QFrame#{} {{ border: 1px solid black; border-radius: 10px; background-color: grey; }}".format(frame.objectName()))



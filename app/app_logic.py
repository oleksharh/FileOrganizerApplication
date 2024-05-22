from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QSize, Qt
from PyQt5.uic import loadUi
from app.custom_title import CustomTitleBar

def load_stylesheet(filename):
    with open(filename, "r") as f:
        return f.read()
    
stylesheet = load_stylesheet("styles/styles.css")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/interface.ui", self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.title_bar)

        self.setStyleSheet(stylesheet)

        self.setWindowPosition()

    def setWindowPosition(self):
        screen = QApplication.desktop().screenGeometry()
        if screen is not None:
            x = int(screen.width() * 0.15)
            y = int(screen.height() * 0.15)
            self.move(x, y)

    def resizeEvent(self, event):
        self.resizeToTwoThirdsOfScreen()
    
    def resizeToTwoThirdsOfScreen(self):
        screen = QApplication.desktop().screenGeometry()
        if screen is not None:
            new_width = screen.width() * 3 / 5
            new_height = screen.height() * 3 / 5
            self.resize(QSize(int(new_width), int(new_height)))
        else:
            self.resize(QSize(1020, 580))
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QSize, Qt
from PyQt5.uic import loadUi
from app.custom_title_bar import CustomTitleBar

from app.constants import MAIN_STYLESHEET

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initializes the MainWindow, loads the UI, and sets up the custom title bar.
        """
        super().__init__()
        loadUi("ui/interface.ui", self)
        
        # Set up a custom title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.title_bar)

        self.setStyleSheet(MAIN_STYLESHEET)

        # Set initial window position and size
        self.setWindowPosition()

    def setWindowPosition(self):
        """
        Positions the window at a specific location relative to the screen.
        """
        screen = QApplication.desktop().screenGeometry()
        if screen is not None:
            x = int(screen.width() * 0.15)
            y = int(screen.height() * 0.15)
            self.move(x, y)

    def resizeEvent(self, event):
        """
        Handles window resizing events by adjusting the window size.
        """
        self.resizeToTwoThirdsOfScreen()
    
    def resizeToTwoThirdsOfScreen(self):
        """
        Resizes the window to two-thirds of the screen size.
        """
        screen = QApplication.desktop().screenGeometry()
        if screen is not None:
            new_width = screen.width() * 3 / 5
            new_height = screen.height() * 3 / 5
            self.resize(QSize(int(new_width), int(new_height)))
        else:
            self.resize(QSize(1020, 580)) # Default size if screen information is not available
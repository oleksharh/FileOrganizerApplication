from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
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

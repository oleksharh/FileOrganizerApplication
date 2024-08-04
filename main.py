import sys
from PyQt5.QtWidgets import QApplication
from app.button_functions import ButtonFunctions

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonFunctions()
    window.show()
    sys.exit(app.exec_())

# TODO add cache to be able to retreive whatever i need faster
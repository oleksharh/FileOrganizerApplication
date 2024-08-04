from PyQt5.QtWidgets import QLineEdit

def load_stylesheet(filename):
    """
    Loads a CSS stylesheet from a file.
    filename: Path to the CSS file
    Returns: CSS stylesheet as a string
    """
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Stylesheet file not found: {filename}")
        return ""

L_E_STYLESHEET = load_stylesheet("styles/l_e_stylesheet.css")

class CustomLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_style = self.styleSheet()
        print(self.original_style)

    def mousePressEvent(self, event):
        self.original_style = self.styleSheet()
        print(self.original_style)
        self.setStyleSheet(L_E_STYLESHEET)
        super().mousePressEvent(event)

    def focusOutEvent(self, event):
        self.setStyleSheet(self.original_style)
        super().focusOutEvent(event)

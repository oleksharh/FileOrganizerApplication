from PyQt5.QtWidgets import QLineEdit
from app.constants import L_E_STYLESHEET, NOTE_STYLESHEET

class CustomLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_style = self.styleSheet()
        self.initial_text = ""
        # print(self.original_style)

    def mousePressEvent(self, event):
        self.initial_text = self.text()
        self.original_style = self.styleSheet()
        if self.original_style == NOTE_STYLESHEET:
            self.setStyleSheet(L_E_STYLESHEET)
        super().mousePressEvent(event)

    def focusOutEvent(self, event):
        current_text = self.text()
        if self.initial_text == current_text:
            if self.original_style == NOTE_STYLESHEET:
                self.setStyleSheet(self.original_style)
        super().focusOutEvent(event)


# TODO fix and make it work when clicked and focused out
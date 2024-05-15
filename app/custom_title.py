from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.mouse_pos = None
        self.setFixedHeight(30)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        icon_label = QLabel()
        icon_label.setPixmap(QPixmap("icons/codesandbox_main.svg"))
        icon_label.setObjectName("icon_label")
        icon_label.setFixedSize(30, 30)
        layout.addWidget(icon_label)

        title_label = QLabel("")
        layout.addWidget(title_label)

        minimize_button = QPushButton("—")
        minimize_button.setObjectName("minimize_button")
        minimize_button.setFixedSize(30, 30)
        minimize_button.clicked.connect(self.parent.showMinimized)
        layout.addWidget(minimize_button)

        close_button = QPushButton("X")
        close_button.setObjectName("close_button")
        close_button.setFixedSize(30, 30)
        close_button.clicked.connect(self.parent.close)
        layout.addWidget(close_button)

    def mousePressEvent(self, event):
        self.mouse_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.mouse_pos:
            delta = event.globalPos() - self.mouse_pos
            self.parent.move(self.parent.pos() + delta)
            self.mouse_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.mouse_pos = None

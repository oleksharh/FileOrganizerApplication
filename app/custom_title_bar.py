from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the custom title bar with window control buttons and icon.
        parent: The parent window (MainWindow)
        """
        super().__init__(parent)
        self.parent = parent
        self.mouse_pos = None
        self.setFixedHeight(30)

        # Set up the layout and add widgets
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Add icon
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap("icons/codesandbox_main.svg"))
        icon_label.setObjectName("icon_label")
        icon_label.setFixedSize(30, 30)
        layout.addWidget(icon_label)

        # Add title label
        title_label = QLabel("")
        layout.addWidget(title_label)

        # Add minimize button
        minimize_button = QPushButton("—")
        minimize_button.setObjectName("minimize_button")
        minimize_button.setFixedSize(30, 30)
        minimize_button.clicked.connect(self.parent.showMinimized)
        layout.addWidget(minimize_button)

        # Add close button
        close_button = QPushButton("X")
        close_button.setObjectName("close_button")
        close_button.setFixedSize(30, 30)
        close_button.clicked.connect(self.parent.close)
        layout.addWidget(close_button)

    def mousePressEvent(self, event):
        """
        Handles the mouse press event to start moving the window.
        """
        self.mouse_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        """
        Handles the mouse move event to update the window position.
        """
        if self.mouse_pos:
            delta = event.globalPos() - self.mouse_pos
            self.parent.move(self.parent.pos() + delta)
            self.mouse_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        """
        Handles the mouse release event to stop moving the window.
        """
        self.mouse_pos = None


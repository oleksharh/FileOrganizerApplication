from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QHBoxLayout, QLabel 
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
 


class HoverButton(QPushButton):
    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet("QPushButton { border: 1px solid black; border-radius: 5px; background-color: grey; }")
        self.normal_style = self.styleSheet()

    def enterEvent(self, event):
        self.setStyleSheet("QPushButton { border: 1px solid black; border-radius: 10px; background-color: lightgrey; }")

    def leaveEvent(self, event):
        self.setStyleSheet(self.normal_style)

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
        icon_label.setFixedSize(30, 30)
        icon_label.setStyleSheet("QLabel { padding: 3px; }")
        layout.addWidget(icon_label)

        title_label = QLabel("")
        layout.addWidget(title_label)

        minimize_button = QPushButton("—")
        minimize_button.setFixedSize(30, 30)
        minimize_button.clicked.connect(self.parent.showMinimized)
        layout.addWidget(minimize_button)

        close_button = QPushButton("X")
        close_button.setFixedSize(30, 30)
        close_button.clicked.connect(self.parent.close)
        layout.addWidget(close_button)

        self.setStyleSheet("""
            QWidget {
                color: #66FCF1;
                font-weight: bold;
            }
            QLabel {
                background-color: transparent;
            }
            QPushButton {
                background-color: transparent;
                color: #66FCF1;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF0000;
                color: white;
            }
        """)

    def mousePressEvent(self, event):
        self.mouse_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.mouse_pos:
            delta = event.globalPos() - self.mouse_pos
            self.parent.move(self.parent.pos() + delta)
            self.mouse_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.mouse_pos = None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Python\FileOrganizerApplication\ui\interface.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.title_bar)

        self.setStyleSheet("QWidget#main_window_body { background-color: #0B0C10; }")

        self.setFrameStyles()
        self.setButtonStyles()
        self.setTextStyles()
        self.setLineEditStyles()
        self.setCheckBoxStyles()

    def setLineEditStyles(self):
        self.src_path_line_edit.setStyleSheet("QLineEdit { background-color: #0B0C10; border: 0px #0B0C10; border-radius: 10px; color: #C5C6C7; }")
        self.dest_path_line_edit.setStyleSheet("QLineEdit { background-color: #0B0C10; border: 0px #0B0C10; border-radius: 10px; color: #C5C6C7; }")

    def setCheckBoxStyles(self):
        self.applyCheckBoxStyles(self.c_gallery)
        self.applyCheckBoxStyles(self.c_zips)
        self.applyCheckBoxStyles(self.c_docs)
        self.applyCheckBoxStyles(self.c_codes)
        self.applyCheckBoxStyles(self.c_3d_files)
        self.applyCheckBoxStyles(self.c_apps)

    def applyCheckBoxStyles(self, check_box):
        check_box.setStyleSheet('''         
        QCheckBox {
            color: #C5C6C7;
        }
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 10px;
            background-color: #0B0C10;
        }
        QCheckBox::indicator:checked {
            background-color: #66FCF1;
        }
    ''')

    def setFrameStyles(self):
        self.applyRoundedCorners(self.frame_4)
        self.applyRoundedCorners(self.frame_2)
        self.applyRoundedCorners(self.frame_3)
        self.applyRoundedCorners(self.frame_5)
        self.applyRoundedCorners(self.frame_6)

    def setTextStyles(self):
        # Blue Colored Text
        self.applyTextColorBlue(self.file_organizer)
        self.applyTextColorBlue(self.src_label)
        self.applyTextColorBlue(self.dest_label)
        self.applyTextColorBlue(self.create_folders_label)
        self.applyTextColorBlue(self.move_label)
        self.applyTextColorBlue(self.to_label)
        self.applyTextColorBlue(self.from_label)

        # Grey Colored Text
        self.applyTextColorGrey(self.other_notice_label)
        self.applyTextColorGrey(self.label_description_src)
        self.applyTextColorGrey(self.label_description_dest)

    def setButtonStyles(self):
        self.applyRoundedCornersAndHoverEffect(self.browse_and_submit_button_1)
        self.applyRoundedCornersAndHoverEffect(self.browse_and_submit_button_2)
        self.applyRoundedCornersAndHoverEffect(self.submit_button)
        self.applyRoundedCornersAndHoverEffect(self.run_button)

    def applyRoundedCorners(self, frame):
        frame.setStyleSheet("QFrame#{} {{ border: 1px solid black; border-radius: 10px; background-color: #1F2833; }}".format(frame.objectName()))

    def applyTextColorBlue(self, label):
        label.setStyleSheet("QLabel { color: #66FCF1; }")

    def applyTextColorGrey(self, label):
        label.setStyleSheet("QLabel { color: #C5C6C7; }")

    def applyRoundedCornersAndHoverEffect(self, button):
        button.setStyleSheet("QPushButton { border: 1px solid black; border-radius: 10px; background-color: #66FCF1; }")
        button.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == event.Enter:
            obj.setStyleSheet("QPushButton { border: 1px solid black; border-radius: 10px; background-color: #45A29E; }")
        elif event.type() == event.Leave:
            obj.setStyleSheet("QPushButton { border: 1px solid black; border-radius: 10px; background-color: #66FCF1; }")
        return super().eventFilter(obj, event)
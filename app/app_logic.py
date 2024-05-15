from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QHBoxLayout, QLabel 
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap

# COLORS:
light_cyan = "#66FCF1"
dark_cyan = "#45A29E"
red_saturated = "#FF0000"
silver = "#C5C6C7"
dark_gray = "#0B0C10"

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
        # icon_label.setStyleSheet("QLabel { padding: 3px; }")
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

        # self.setStyleSheet(f"""
        #     QLabel {{
        #         background-color: transparent;
        #     }}
        #     QPushButton {{
        #         background-color: transparent;
        #         color: {light_cyan};
        #         border: none;
        #         font-weight: bold;
        #     }}
        #     QPushButton:hover {{
        #         background-color: {red_saturated};
        #         color: white;
        #         font-weight: bold;
        #     }}
        #     QPushButton#minimize_button:hover {{
        #         background-color: {silver};
        #         color: black;
        #         font-weight: bold;
        #     }}
        # """)

        

    def mousePressEvent(self, event):
        self.mouse_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.mouse_pos:
            delta = event.globalPos() - self.mouse_pos
            self.parent.move(self.parent.pos() + delta)
            self.mouse_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.mouse_pos = None

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

    #     self.setStyleSheet(f"QWidget#main_window_body {{ background-color: {dark_gray}; }}")

    #     self.setFrameStyles()
    #     self.setButtonStyles()
    #     self.setTextStyles()
    #     self.setLineEditStyles()
    #     self.setCheckBoxStyles()

    # def setLineEditStyles(self):
    #     self.src_path_line_edit.setStyleSheet(f"QLineEdit {{ background-color: {dark_gray}; border: 0px {dark_gray}; border-radius: 10px; color: {silver}; }}")
    #     self.dest_path_line_edit.setStyleSheet(f"QLineEdit {{ background-color: {dark_gray}; border: 0px {dark_gray}; border-radius: 10px; color: {silver}; }}")

    # def setCheckBoxStyles(self):
    #     self.applyCheckBoxStyles(self.c_gallery)
    #     self.applyCheckBoxStyles(self.c_zips)
    #     self.applyCheckBoxStyles(self.c_docs)
    #     self.applyCheckBoxStyles(self.c_codes)
    #     self.applyCheckBoxStyles(self.c_3d_files)
    #     self.applyCheckBoxStyles(self.c_apps)

    # def applyCheckBoxStyles(self, check_box):
    #     check_box.setStyleSheet(f'''         
    #     QCheckBox {{
    #         color: {silver};
    #     }}
    #     QCheckBox::indicator {{
    #         width: 20px;
    #         height: 20px;
    #         border-radius: 10px;
    #         background-color: {dark_gray};
    #     }}
    #     QCheckBox::indicator:checked {{
    #         background-color: {light_cyan};
    #     }}
    # ''')

    # def setFrameStyles(self):
    #     self.applyRoundedCorners(self.frame_4)
    #     self.applyRoundedCorners(self.frame_2)
    #     self.applyRoundedCorners(self.frame_3)
    #     self.applyRoundedCorners(self.frame_5)
    #     self.applyRoundedCorners(self.frame_6)

    # def setTextStyles(self):
    #     # Blue Colored Text
    #     self.applyTextColorBlue(self.file_organizer)
    #     self.applyTextColorBlue(self.src_label)
    #     self.applyTextColorBlue(self.dest_label)
    #     self.applyTextColorBlue(self.create_folders_label)
    #     self.applyTextColorBlue(self.move_label)
    #     self.applyTextColorBlue(self.to_label)
    #     self.applyTextColorBlue(self.from_label)

    #     # Grey Colored Text
    #     self.applyTextColorGrey(self.other_notice_label)
    #     self.applyTextColorGrey(self.label_description_src)
    #     self.applyTextColorGrey(self.label_description_dest)

    # def setButtonStyles(self):
    #     self.applyRoundedCornersAndHoverEffect(self.browse_and_submit_button_1)
    #     self.applyRoundedCornersAndHoverEffect(self.browse_and_submit_button_2)
    #     self.applyRoundedCornersAndHoverEffect(self.submit_button)
    #     self.applyRoundedCornersAndHoverEffect(self.run_button)
    #     self.applyRoundedCornersAndHoverEffect(self.tick_all_button)

    # def applyRoundedCorners(self, frame):
    #     frame.setStyleSheet("QFrame#{} {{ border: 1px solid black; border-radius: 10px; background-color: #1F2833; }}".format(frame.objectName()))

    # def applyTextColorBlue(self, label):
    #     label.setStyleSheet(f"QLabel {{ color: {light_cyan}; }}")

    # def applyTextColorGrey(self, label):
    #     label.setStyleSheet(f"QLabel {{ color: {silver}; }}")

    # def applyRoundedCornersAndHoverEffect(self, button):
    #     button.setStyleSheet(f"QPushButton {{ border: 1px solid black; border-radius: 10px; background-color: {light_cyan}; }}")
    #     button.installEventFilter(self)

    # def eventFilter(self, obj, event):
    #     if event.type() == event.Enter:
    #         obj.setStyleSheet(f"QPushButton {{ border: 1px solid black; border-radius: 10px; background-color: {dark_cyan}; }}")
    #     elif event.type() == event.Leave:
    #         obj.setStyleSheet(f"QPushButton {{ border: 1px solid black; border-radius: 10px; background-color: {light_cyan}; }}")
    #     return super().eventFilter(obj, event)

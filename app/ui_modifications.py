from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        loadUi(r"C:\Python\FileOrganizerApplication\ui\main_window.ui", self)
        self.setWindowTitle("FileOrganizer")         

        #Responsive Main Widget
        #-------------------------------------------------------------------------------------------------------
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QGridLayout(central_widget)

        left_upper_widget = QWidget()
        self.main_layout.addWidget(left_upper_widget, 0, 0)
        self.left_upper_element = QGridLayout()
        self.left_upper_element.addWidget(self.label_choose_src, 1, 1, 1, 2)
        self.left_upper_element.addWidget(self.src_path_line_edit, 2, 1)
        self.left_upper_element.addWidget(self.browse_and_submit_button_1, 2, 2)
        self.left_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 3, 0)
        self.left_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        self.left_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        self.left_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 3)
        self.main_layout.addLayout(self.left_upper_element, 0, 0)

        right_upper_widget = QWidget()
        self.main_layout.addWidget(right_upper_widget, 0, 1)
        self.right_upper_element = QGridLayout()
        self.right_upper_element.addWidget(self.label_choose_dest, 1, 1, 1 ,2)
        self.right_upper_element.addWidget(self.dest_path_line_edit, 2, 1)
        self.right_upper_element.addWidget(self.browse_and_submit_button_2, 2, 2)
        self.right_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 3, 0)
        self.right_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        self.right_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        self.right_upper_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 3)
        self.main_layout.addLayout(self.right_upper_element, 0, 1)

        left_lower_widget = QWidget()
        self.main_layout.addWidget(left_lower_widget, 1, 0)
        self.left_lower_element = QGridLayout()
        self.left_lower_element.addWidget(self.label_folders_create, 1, 1, 1, 2)
        self.left_lower_element.addWidget(self.c_zip, 2, 1)
        self.left_lower_element.addWidget(self.c_docs, 3, 1)
        self.left_lower_element.addWidget(self.c_gallery, 4, 1)
        self.left_lower_element.addWidget(self.c_codes, 5, 1)
        self.left_lower_element.addWidget(self.c_3d_files, 6, 1)
        self.left_lower_element.addWidget(self.c_apps, 7, 1)
        self.left_lower_element.addWidget(self.submit_button, 2, 2, 4, 1)
        self.submit_button.setStyleSheet("text-align: center; vertical-align: middle;")
        self.left_lower_element.addWidget(self.label_result_create, 5, 2, 3, 1)
        self.left_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        self.left_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        self.left_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 8, 1)
        self.left_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 3)
        self.main_layout.addLayout(self.left_lower_element, 1,0)        

        right_lower_widget = QWidget()
        self.main_layout.addWidget(right_lower_widget, 1, 1)
        self.right_lower_element = QGridLayout()
        self.right_lower_element.addWidget(self.label_organize_files, 1, 1)
        self.right_lower_element.addWidget(self.label_description, 2, 1)
        self.right_lower_element.addWidget(self.run_button, 3, 1)
        self.right_lower_element.addWidget(self.label_result_organize, 4, 1)
        self.right_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        self.right_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        self.right_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 5, 1)
        self.right_lower_element.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2)
        self.main_layout.addLayout(self.right_lower_element, 1, 1)


        # Set alignment for all labels
        self.label_choose_src.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.label_choose_dest.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.label_folders_create.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.label_organize_files.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        right_lower_widget.setStyleSheet("border: 1px solid black; background-color: green;")
        left_lower_widget.setStyleSheet("border: 1px solid black; background-color: blue;")
        right_upper_widget.setStyleSheet("border: 1px solid black; background-color: yellow;")
        left_upper_widget.setStyleSheet("border: 1px solid black; background-color: red;")
        #-------------------------------------------------------------------------------------------------------

        self.setMinimumSize(640, 480)
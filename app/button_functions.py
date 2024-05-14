from PyQt5.QtWidgets import QFileDialog
from app.organizer import modify_dest, define_chosen_directories, modify_src, create_folders, move_files
from app.ui_modifications import MainWindow
import os
from PyQt5.QtCore import QTimer

class ButtonFunctions(MainWindow):
    def __init__(self):
        super().__init__()
        
        self.browse_and_submit_button_1.clicked.connect(self.src_browse_button)
        self.browse_and_submit_button_2.clicked.connect(self.dest_browse_button)   
        self.submit_button.clicked.connect(self.submit_create_directories)
        self.run_button.clicked.connect(self.run_move_files)
        self.tick_all_button.clicked.connect(self.tick_all)

    def src_browse_button(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Choose Source Folder", r"C:/")
        if folder_path:
            self.src_path_line_edit.setText(folder_path)
            new_value_src = self.src_path_line_edit.text()
            modify_src(new_value_src)

            new_value_dest = self.dest_path_line_edit.text()
            modify_dest(new_value_dest)
            self.label_description_src.setText(new_value_src)
            self.label_description_dest.setText(new_value_dest)

    def dest_browse_button(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Choose Destination Folder", r"C:/")
        if folder_path:
            self.dest_path_line_edit.setText(folder_path)
            new_value_src = self.src_path_line_edit.text()
            modify_src(new_value_src)

            new_value_dest = self.dest_path_line_edit.text()
            modify_dest(new_value_dest)
            self.label_description_src.setText(new_value_src)
            self.label_description_dest.setText(new_value_dest)

    def submit_create_directories(self):
        if os.path.isdir(self.dest_path_line_edit.text()):
            checked_buttons = [
                self.c_gallery.isChecked(),
                self.c_zips.isChecked(),
                self.c_docs.isChecked(),
                self.c_codes.isChecked(),
                self.c_3d_files.isChecked(),
                self.c_apps.isChecked()
            ]

            define_chosen_directories(checked_buttons)
            create_folders()
            
            self.submit_button.setText("Successfuly created")
        else:
            self.submit_button.setText("Define destination directory!!!")
            QTimer.singleShot(1300, lambda: self.submit_button.setText("Submit"))

    def tick_all(self):
        checkbox_list = [self.c_gallery, self.c_zips, self.c_docs, self.c_codes, self.c_3d_files, self.c_apps]
        all_checked = all(check_box.isChecked() for check_box in checkbox_list)

        if all_checked:
            for checkbox in checkbox_list:
                checkbox.setChecked(False)
            self.tick_all_button.setText('Tick All')
        else:
            for checkbox in checkbox_list:
                checkbox.setChecked(True)
            self.tick_all_button.setText('Untick All')

    def run_move_files(self):
        if os.path.isdir(self.src_path_line_edit.text()) and os.path.isdir(self.dest_path_line_edit.text()):
            move_files(self.dest_path_line_edit.text())
            self.run_button.setText("Completed Successfuly")
        else:
            self.run_button.setText("Define directories!!!")
            QTimer.singleShot(1300, lambda: self.run_button.setText("Run"))

    
            
        
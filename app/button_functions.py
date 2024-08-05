import os
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog
from app.organizer import (
    modify_dest,
    define_chosen_directories,
    modify_src,
    create_folders,
    move_files,
)
from app.app_init import MainWindow
from app.utils import open_directory_dialog
from app.constants import ERROR_SYLESHEET, SUCCESS_SYLESHEET, NOTE_STYLESHEET, L_E_STYLESHEET, DEFAULT_DIR

class ButtonFunctions(MainWindow):
    def __init__(self):
        super().__init__()
        # Set up signal connections for UI elements
        self.setup_connections()

        # Set placeholder text for the line edit fields
        self.setup_placeholders()

    def setup_connections(self):
        '''
        Connect buttons to their respective functions
        '''
        self.browse_and_submit_button_1.clicked.connect(self.browse_button_func)
        self.browse_and_submit_button_2.clicked.connect(self.browse_button_func)
        self.src_path_line_edit.textChanged.connect(self.on_text_changed)
        self.dest_path_line_edit.textChanged.connect(self.on_text_changed)
        self.submit_button1.clicked.connect(self.submit_create_directories)
        self.submit_button2.clicked.connect(self.run_move_files)
        self.tick_all_button.clicked.connect(self.tick_all)

    def setup_placeholders(self):
        '''
        Set placeholder text for the line edit fields
        '''
        self.src_path_line_edit.setPlaceholderText("Enter source directory...")
        self.dest_path_line_edit.setPlaceholderText("Enter destination directory...")

    def browse_button_func(self):
        '''
        Determine which button triggered the 
        function and open directory dialog
        '''
        sender = self.sender()
        line_edit, title_text = self.get_line_edit_and_title(sender.objectName())
        folder_path = open_directory_dialog(self, title_text, DEFAULT_DIR)
        if folder_path:
            line_edit.setText(folder_path)

    def get_line_edit_and_title(self, sender_name):
        '''
        Return appropriate line edit 
        and title based on sender name
        '''
        if sender_name == "browse_and_submit_button_1":
            return self.src_path_line_edit, "Choose Source Directory"
        elif sender_name == "browse_and_submit_button_2":
            return self.dest_path_line_edit, "Choose Destination Directory"

    def on_text_changed(self, text):
        '''
        Update the stylesheet based 
        on whether the path exists
        '''
        if os.path.exists(text):
            self.sender().setStyleSheet(SUCCESS_SYLESHEET)
            if self.sender().objectName() == "src_path_line_edit":
                self.update_src_directory(text)
            elif self.sender().objectName() == "dest_path_line_edit":
                self.update_dest_directory(text)
        else:
            self.sender().setStyleSheet(L_E_STYLESHEET)

    def update_src_directory(self, new_value_src):
        '''
        Update source directory
        '''
        modify_src(new_value_src)
        self.label_description_src.setText(new_value_src)

    def update_dest_directory(self, new_value_dest):
        '''
        Update destination directory
        '''
        modify_dest(new_value_dest)
        self.label_description_dest.setText(new_value_dest)

    def submit_create_directories(self):
        '''
        Check if destination directory 
        exists and create directories
        '''
        if os.path.isdir(self.dest_path_line_edit.text()):
            self.create_directories()
        else:
            self.show_error("Define destination directory!!!", self.submit_button1)
            self.src_path_line_edit.setStyleSheet(NOTE_STYLESHEET)
            self.dest_path_line_edit.setStyleSheet(NOTE_STYLESHEET)

    def create_directories(self):
        '''
        Create directories based 
        on checked buttons
        '''
        checked_buttons = [
            self.c_gallery.isChecked(),
            self.c_zips.isChecked(),
            self.c_docs.isChecked(),
            self.c_codes.isChecked(),
            self.c_3d_files.isChecked(),
            self.c_apps.isChecked(),
        ]
        dest_dir = self.dest_path_line_edit.text()
        define_chosen_directories(dest_dir, checked_buttons)
        create_folders()
        self.show_success("Successfully Created", self.submit_button1)

    def tick_all(self):
        '''
        Toggle all checkboxes
        '''
        checkbox_list = [
            self.c_gallery,
            self.c_zips,
            self.c_docs,
            self.c_codes,
            self.c_3d_files,
            self.c_apps,
        ]
        all_checked = all(check_box.isChecked() for check_box in checkbox_list)
        for checkbox in checkbox_list:
            checkbox.setChecked(not all_checked)
        self.tick_all_button.setText("Untick All" if not all_checked else "Tick All")

    def run_move_files(self):
        '''
        Validate directories and move files
        '''
        if self.directories_are_valid():
            if move_files(self.dest_path_line_edit.text()):
                self.show_success("Completed Successfully", self.submit_button2)
            else:
                self.show_error("Define directories!!!", self.submit_button2)
        else:
            self.show_error("Define directories!!!", self.submit_button2)

    def directories_are_valid(self):
        '''
        Check if both source and destination 
        directories are valid
        '''
        return os.path.isdir(self.src_path_line_edit.text()) and os.path.isdir(self.dest_path_line_edit.text())

    def show_success(self, message, button):
        '''
        Show success message on the button
        '''
        self.update_button(button, message, SUCCESS_SYLESHEET)

    def show_error(self, message, button):
        '''
        Show error message on the button
        '''
        self.update_button(button, message, ERROR_SYLESHEET)

    def update_button(self, button, text, stylesheet):
        '''
        Update button text, disable 
        it and apply stylesheet
        '''
        button.setText(text)
        button.setEnabled(False)
        button.setStyleSheet(stylesheet)
        QTimer.singleShot(1300, lambda: self.reset_button(button))

    def reset_button(self, button):
        '''
        Reset button to its original state
        '''
        button.setStyleSheet("")
        button.setEnabled(True)
        button.setText("Submit")

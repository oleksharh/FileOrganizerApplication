import os
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer
from app.organizer import (
    modify_dest,
    define_chosen_directories,
    modify_src,
    create_folders,
    move_files,
)
from app.app_init import MainWindow



button_error = "background-color: #FF0000; color: white; font-weight: bold;"
button_success = "background-color: #00FF00; color: 000000; font-weight: bold;"


class ButtonFunctions(MainWindow):
    def __init__(self):
        super().__init__()
        
        # Connect buttons to their respective functions
        self.browse_and_submit_button_1.clicked.connect(
            lambda: self.browse_button_func(
                self.src_path_line_edit, "Choose Source Directory"
            )
        )
        self.browse_and_submit_button_2.clicked.connect(
            lambda: self.browse_button_func(
                self.dest_path_line_edit, "Choose Destination Directory"
            )
        )
        self.submit_button1.clicked.connect(self.submit_create_directories)
        self.submit_button2.clicked.connect(self.run_move_files)
        self.tick_all_button.clicked.connect(self.tick_all)

    def browse_button_func(self, line_edit_name, title_text):
        """
        Opens a directory selection dialog and sets the selected path in the line edit.
        """
        folder_path = QFileDialog.getExistingDirectory(self, title_text, r"C:/")
        if folder_path:
            line_edit_name.setText(folder_path)

            # Update source and destination directories
            new_value_src = self.src_path_line_edit.text()
            modify_src(new_value_src)

            new_value_dest = self.dest_path_line_edit.text()
            modify_dest(new_value_dest)

            # Update labels in the UI with selected paths
            self.label_description_src.setText(new_value_src)
            self.label_description_dest.setText(new_value_dest)

    def submit_create_directories(self):
        """
        Validates and creates directories based on user selection.
        """
        if os.path.isdir(self.dest_path_line_edit.text()):
            checked_buttons = [
                self.c_gallery.isChecked(),
                self.c_zips.isChecked(),
                self.c_docs.isChecked(),
                self.c_codes.isChecked(),
                self.c_3d_files.isChecked(),
                self.c_apps.isChecked(),
            ]

            define_chosen_directories(checked_buttons)
            create_folders()

            self.output_submit_button(
                self.submit_button1, "Successfully Created", button_success
            )
            QTimer.singleShot(
                1300, lambda: self.reset_submit_button(self.submit_button1)
            )
        else:
            self.output_submit_button(
                self.submit_button1, "Define destination directory!!!", button_error
            )
            QTimer.singleShot(
                1300, lambda: self.reset_submit_button(self.submit_button1)
            )

    def tick_all(self):
        """
        Toggles all checkboxes.
        """
        checkbox_list = [
            self.c_gallery,
            self.c_zips,
            self.c_docs,
            self.c_codes,
            self.c_3d_files,
            self.c_apps,
        ]
        
        all_checked = all(check_box.isChecked() for check_box in checkbox_list)

        if all_checked:
            for checkbox in checkbox_list:
                checkbox.setChecked(False)
            self.tick_all_button.setText("Tick All")
        else:
            for checkbox in checkbox_list:
                checkbox.setChecked(True)
            self.tick_all_button.setText("Untick All")

    def run_move_files(self):
        """
        Moves files from the source to the destination directories.
        Essentially initializing move_files in organizer.py file
        """
        if os.path.isdir(self.src_path_line_edit.text()) and os.path.isdir(
            self.dest_path_line_edit.text()
        ):
            move_files_var = move_files(self.dest_path_line_edit.text())

            if move_files_var:
                self.output_submit_button(
                    self.submit_button2, "Completed Successfully", button_success
                )
                QTimer.singleShot(
                    1300, lambda: self.reset_submit_button(self.submit_button2)
                )
            else:
                self.output_submit_button(
                self.submit_button2, "Define directories!!!", button_error
                )
                QTimer.singleShot(
                    1300, lambda: self.reset_submit_button(self.submit_button2)
                )
        else:
            self.output_submit_button(
                self.submit_button2, "Define directories!!!", button_error
            )
            QTimer.singleShot(
                1300, lambda: self.reset_submit_button(self.submit_button2)
            )

    def reset_submit_button(self, button):
        """
        Resets the submit button to its original state.
        """
        button.setStyleSheet("")
        button.setEnabled(True)
        button.setText("Submit")

    def output_submit_button(self, button, text, stylesheet):
        """
        Updates the submit button with the provided text and stylesheet.
        """
        button.setText(text)
        button.setEnabled(False)
        button.setStyleSheet(stylesheet)

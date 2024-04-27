from PyQt5.QtWidgets import QFileDialog
from app.organizer import modify_dest, define_chosen_directories, modify_src, create_folders, move_files
from app.ui_modifications import MainWindow

class ButtonFunctions(MainWindow):
    def __init__(self):
        super().__init__()

        self.browse_and_submit_button_1.clicked.connect(self.src_browse_button)
        self.browse_and_submit_button_2.clicked.connect(self.dest_browse_button)   
        self.submit_button.clicked.connect(self.submit_create_directories)
        self.run_button.clicked.connect(self.run_move_files)

    def src_browse_button(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Choose Source Folder", r"C:/")
        if folder_path:
            self.src_path_line_edit.setText(folder_path)

    def dest_browse_button(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Choose Destination Folder", r"C:/")
        if folder_path:
            self.dest_path_line_edit.setText(folder_path)
            new_value_src = self.src_path_line_edit.text()
            modify_src(new_value_src)

            new_value_dest = self.dest_path_line_edit.text()
            modify_dest(new_value_dest)
            self.label_description.setText(f"Moving from {new_value_src} to {new_value_dest}")

    def submit_create_directories(self):
        
        checked_buttons = [
            self.c_gallery.isChecked(),
            self.c_zip.isChecked(),
            self.c_docs.isChecked(),
            self.c_codes.isChecked(),
            self.c_3d_files.isChecked(),
            self.c_apps.isChecked()
        ]

        new_value_src = self.src_path_line_edit.text()
        modify_src(new_value_src)

        new_value_dest = self.dest_path_line_edit.text()
        modify_dest(new_value_dest)
        
        self.src_path_line_edit.clear()
        self.dest_path_line_edit.clear()

        self.label_description.setText(f"Moving from {new_value_src} to {new_value_dest}")

        define_chosen_directories(checked_buttons)

        create_folders()

        self.label_result_create.setText("Folders have been successfuly created")

    def run_move_files(self):
        self.label_result_organize.setText("Completed Successfuly")

        move_files()
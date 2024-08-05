from PyQt5.QtWidgets import QFileDialog

def load_stylesheet(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Stylesheet file not found: {filename}")
        return ""

def open_directory_dialog(parent, title, initial_dir):
    return QFileDialog.getExistingDirectory(parent, title, initial_dir)

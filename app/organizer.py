import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src_dir = None

def modify_src(new_value: str):
    global src_dir
    src_dir = new_value
    print(src_dir)

dest_dir = None

def modify_dest(new_value: str):
    global dest_dir
    dest_dir = new_value
    print(dest_dir)

(dest_zip, dest_documents, dest_photos, dest_videos, 
dest_codes, dest_threeD, dest_applications, dest_other) = [None] * 8
folders = []
file_types = dict()

# DEFINES FOLDERS TO BE CREATED IF DESTINATION DIRECTORY 
# IS EMPTY AND USER CHOSE TO CREATE THEM
def define_chosen_directories(checked_boxes: list):
    checked_copy = checked_boxes[:]
    checked_copy.insert(0, checked_boxes[0])

    if dest_dir is not None and src_dir is not None:

        dest_to_create = {
            'dest_photos': dest_dir + r"/Gallery/Photos",
            'dest_videos': dest_dir + r"/Gallery/Videos",
            'dest_zip': dest_dir + r"/Zip",
            'dest_documents': dest_dir + r"/Documents",
            'dest_codes': dest_dir + r"/Codes",
            'dest_threeD': dest_dir + r"/3D",
            'dest_applications': dest_dir + r"/Applications"
        }

        for variable, path in dest_to_create.items():
            if checked_copy[0]:
                globals()[variable] = path
                checked_copy.pop(0)
                folders.append(globals()[variable])
                print(folders)
            else:
                checked_copy.pop(0)
        print("done")

# | File extensions to use while sorting |
zips = ["zip"]
documents = ["xlsx", "pdf", "txt", "pptx", "docx"]
photos = ["png", "jpg", "jpeg", "jpeg", "bmp", "gif", "tiff ", "tif", "raw", "cr2", "nef", "arw", "psd"]
videos = ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'mpeg', 'mpg', 'm4v']
codes = ['py', 'cpp', 'c', 'java', 'html', 'css', 'js', 'php', 'rb', 'swift', "sql", "csv", "circ", "asm"]
threeD = ['obj', 'stl', 'fbx', 'blend', 'dae', '3ds', 'ply', 'max', 'ma', 'x3d', "blend1"]
applications = ['exe', 'dmg', 'apk', 'app', 'deb', 'rpm', 'msi', 'bin', 'jar', 'sh']

# FUNCTION TO CREATE FOLDERS IN TEH DIRECTORY PATH(FOLDER)
def create_folders():
    for folder_path in folders:
        os.makedirs(folder_path, exist_ok=True)

def dest_folders_list(dest_dir: str):

    file_types_attributes = [
            ("gallery","photos", photos),
            ("gallery", "videos", videos),
            ("zip", "zip", zips),
            ("documents", "documents", documents),
            ("codes", "codes", codes),
            ("3d","threeD", threeD),
            ("applications", "applications", applications),
            ]

    for folder in os.listdir(dest_dir):
        for folder_name, category, extension in file_types_attributes:
            if folder.lower() == folder_name:
                globals()["dest_" + category] = dest_dir + "/" + folder
                file_types.update({category: extension})

def move_files(dest_dir: str):
    dest_folders_list(dest_dir)
    print(file_types)

    for file in os.listdir(src_dir):

        file_path = os.path.join(src_dir, file)

        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1].lower()
            print(file_extension)
            
            dest_other = dest_dir + r"/Other"
            destination = dest_other
            
            print(file_types)
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination = globals()["dest_" + category]
                    break

            print(destination, file)
            destination_path = os.path.join(destination, file)

            try:
                if not file_extension == 'part':
                    if os.path.exists(destination_path):

                        file_name_parts = file.split('.')[:-1]  
                        file_name_to_change = '.'.join(file_name_parts) + '-Copy'  
                        file_name_final = file_name_to_change + '.' + file_extension  
                        destination_path = os.path.join(destination, file_name_final) 
                        # | 4 lines above change name of a file by adding                      |
                        # | -Copy suffixs so it can be then moved to the destination directory |


                        shutil.move(file_path, destination_path)
                    else:
                        shutil.move(file_path, destination_path)
                else:
                    print("1")
            except PermissionError:
                print("2")
            except FileNotFoundError:
                print("3")

# if __name__ == "__main__":

#     event_handler = FileSystemEventHandler()

#     if not run_create_folders:
#         create_folders(dest_dir)
#         run_create_folders = True
#         print("Folders have been created")

#     def on_modified(event):
#         move_files(src_dir)

#     event_handler.on_modified = on_modified 

#     observer = Observer() 
#     observer.schedule(event_handler, src_dir, recursive=False) # recursive=False - only watches the directory itself, recursive=True - watches the directory and all subdirectories
#     observer.start() 

#     try: 
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()

#     observer.join()




######################################################## Script to create it as executable,
###  pyinstaller --onefile --noconsole organizer.py  ### but before running it, make sure
######################################################## that you have pyinstaller module installed
                                                        
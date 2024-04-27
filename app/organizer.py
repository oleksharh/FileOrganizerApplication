import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src_dir = None

def modify_src(new_value):
    global src_dir
    src_dir = new_value
    print(src_dir)

dest_dir = None

def modify_dest(new_value):
    global dest_dir
    dest_dir = new_value
    print(dest_dir)

dest_zip, dest_documents, dest_photos, dest_videos, dest_codes, dest_threeD, dest_applications, dest_other = [None] * 8
folders = []

# DESTINATION FOLDERS AND EXTENSIONS FOR THEM
#_______________________________________________________________________________________________________________________
# | Destination directories, rename them as you wish to match your needs |     
def define_chosen_directories(checked_boxes):
    checked_copy = checked_boxes[:]
    checked_copy.insert(0, checked_boxes[0])
    checked_copy.append(True)

    if dest_dir is not None and src_dir is not None:       

        dest_to_create = {
            'dest_photos': dest_dir + r"/Gallery/Photos",
            'dest_videos': dest_dir + r"/Gallery/Videos",
            'dest_zip': dest_dir + r"/Zip",
            'dest_documents': dest_dir + r"/Documents",
            'dest_codes': dest_dir + r"/Codes",
            'dest_threeD': dest_dir + r"/3D",
            'dest_applications': dest_dir + r"/Applications",
            'dest_other': dest_dir + r"/Other"
        }

        for variable, path in dest_to_create.items():
            if checked_copy[0]:
                globals()[variable] = path
                checked_copy.pop(0)
                folders.append(globals()[variable])
                print(folders)
            else:
                checked_copy.pop(0)

# | File types to match directories above |
zips = ["zip"]
documents = ["xlsx", "pdf", "txt", "pptx", "docx"]
photos = ["png", "jpg", "jpeg", "jpeg", "bmp", "gif", "tiff ", "tif", "raw", "cr2", "nef", "arw", "psd"]
videos = ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'mpeg', 'mpg', 'm4v']
codes = ['py', 'cpp', 'c', 'java', 'html', 'css', 'js', 'php', 'rb', 'swift', "sql", "csv", "circ", "asm"]
threeD = ['obj', 'stl', 'fbx', 'blend', 'dae', '3ds', 'ply', 'max', 'ma', 'x3d', "blend1"]
applications = ['exe', 'dmg', 'apk', 'app', 'deb', 'rpm', 'msi', 'bin', 'jar', 'sh']


# | One time function to create              |
# | the folders in the destination directory |
def create_folders():
    # | Creates path in the destination directory |
    # | so it then can be used to move files into |
    for folder_path in folders:
        os.makedirs(folder_path, exist_ok=True)


# | Function that is executed on the        |
# | event of modifying the source directory |
def move_files():

    file_types = {
        "documents": documents,
        "photos": photos,
        "videos": videos,
        "codes": codes,
        "threeD": threeD,
        "applications": applications,
        "zip": zips
        # |Change the name of the keys  |
        # |to match the folder name for |
        # |your custom folder that you  |
        # |have created earlier         |
    }

    for file in os.listdir(src_dir):

        file_path = os.path.join(src_dir, file)

        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1].lower()

            destination = dest_other

            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination = globals()["dest_" + category]
                    break

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
                    time.sleep(1)
                    move_files(src_dir)
            except PermissionError:
                time.sleep(1)
                move_files(src_dir)
            except FileNotFoundError:
                time.sleep(1)
                move_files(src_dir)

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
                                                        
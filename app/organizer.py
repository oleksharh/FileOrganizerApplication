import os
import shutil

# Define source and destination directories as global variables
src_dir = None
dest_dir = None

def modify_src(new_value: str):
    """
    Modifies the source directory.
    new_value: New source directory path
    """
    global src_dir
    src_dir = new_value
    print(f"Source directory set to: {src_dir}")

def modify_dest(new_value: str):
    """
    Modifies the destination directory.
    new_value: New destination directory path
    """
    global dest_dir
    dest_dir = new_value
    print(f"Destination directory set to: {dest_dir}")

# Define folder variables and lists to store folder paths and file types
dest_zips, dest_documents, dest_photos, dest_videos, dest_codes, dest_threeD, dest_applications, dest_other = [None] * 8
folders = []
file_types = dict()



def define_chosen_directories(checked_boxes: list):
    """
    Defines folders to be created in the destination directory.
    checked_boxes: List of booleans indicating which folders to create
    """
    checked_copy = checked_boxes[:] # Copy the list of checked boxes
    checked_copy.insert(0, checked_boxes[0])

    if dest_dir is not None and src_dir is not None:

        dest_to_create = {
            'dest_photos': dest_dir + r"/Gallery/Photos",
            'dest_videos': dest_dir + r"/Gallery/Videos",
            'dest_zips': dest_dir + r"/Zips",
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
                print(f"Folder to create: {folders}")
            else:
                checked_copy.pop(0)
        
        folders.append(os.path.join(dest_dir, "Other"))
        print("Done defining folders.")



# Define file extensions for each folder category
zips = ["zip"]
documents = ["xlsx", "pdf", "txt", "pptx", "docx"]
photos = ["png", "jpg", "jpeg", "jpeg", "bmp", "gif", "tiff ", "tif", "raw", "cr2", "nef", "arw", "psd"]
videos = ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'mpeg', 'mpg', 'm4v']
codes = ['py', 'cpp', 'c', 'java', 'html', 'css', 'js', 'php', 'rb', 'swift', "sql", "csv", "circ", "asm"]
threeD = ['obj', 'stl', 'fbx', 'blend', 'dae', '3ds', 'ply', 'max', 'ma', 'x3d', "blend1"]
applications = ['exe', 'dmg', 'apk', 'app', 'deb', 'rpm', 'msi', 'bin', 'jar', 'sh']



def create_folders():
    """
    Creates folders in the destination directory.
    """
    for folder_path in folders:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")



def dest_folders_list(dest_dir: str):
    """
    Populates the file_types dictionary with folder paths
    and their respective file extensions.
    dest_dir: Destination directory path
    """
    file_types_attributes = [
            ("gallery","photos", photos),
            ("gallery", "videos", videos),
            ("zips", "zips", zips),
            ("documents", "documents", documents),
            ("codes", "codes", codes),
            ("3d","threeD", threeD),
            ("applications", "applications", applications),
    ]

    for folder in os.listdir(dest_dir):
        for folder_name, category, extension in file_types_attributes:
            if folder.lower() == folder_name:
                globals()["dest_" + category] = os.path.join(dest_dir, folder)
                file_types.update({category: extension})



def move_files(dest_dir: str):
    """
    Moves files from the source to the destination folders,
    sorting them based on their extensions.
    dest_dir: Destination directory path
    """
    dest_folders_list(dest_dir)
    print(f"File types to be sorted: {file_types}")

    folder_other_exists = "Other" in os.listdir(dest_dir)

    if folder_other_exists:
        for file in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file)

            if os.path.isfile(file_path):
                file_extension = file.split('.')[-1].lower()
                print(f"Processing file with extension: {file_extension}")
                
                dest_other = os.path.join(dest_dir, "Other")
                destination = dest_other
                
                for category, extensions in file_types.items():
                    if file_extension in extensions:
                        destination = globals()["dest_" + category]
                        break

                destination_path = os.path.join(destination, file)
                print(f"Moving file to: {destination_path}")

                try:
                    if not file_extension == 'part':
                        if os.path.exists(destination_path):
                            file_name_parts = file.split('.')[:-1]
                            file_name_to_change = '.'.join(file_name_parts) + '-Copy'
                            file_name_final = file_name_to_change + '.' + file_extension
                            destination_path = os.path.join(destination, file_name_final)

                            shutil.move(file_path, destination_path)
                        else:
                            shutil.move(file_path, destination_path)
                except PermissionError:
                    print(f"PermissionError: Cannot move {file}")
                except FileNotFoundError:
                    print(f"FileNotFoundError: {file} not found")
    else:
        return False

    return True




# TODO - Add Copy suffix if file already exists; - Add progress bar; - Add skipping of corrupted files; - Check space in the dest to src to be able to move sufficiently;
# TODO - ADD configuration options (User would be able to chose their own); - Add logs for user understanding and further debugging
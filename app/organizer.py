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

def folders_exist(dest_dir):
    '''
    Checks if some folders already exist in the
    destination directory and returns bool list
    so define_chosen_directories can be more 
    efficient and viable
    '''
    checked_folders = [False for i in range(7)]

    if dest_dir is not None:
        checked_folders = []

        dest_to_create = {
                'dest_photos': dest_dir + r"/Gallery/Photos",
                'dest_videos': dest_dir + r"/Gallery/Videos",
                'dest_zips': dest_dir + r"/Zips",
                'dest_documents': dest_dir + r"/Documents",
                'dest_codes': dest_dir + r"/Codes",
                'dest_threeD': dest_dir + r"/3D",
                'dest_applications': dest_dir + r"/Applications"
            }

        for path in dest_to_create.values():
            if os.path.exists(path):
                checked_folders.append(True)
            else:
                checked_folders.append(False)

    return checked_folders

def define_chosen_directories(dest_dir, checked_boxes: list):
    """
    Defines folders to be created in the destination directory.
    checked_boxes: List of booleans indicating which folders to create
    """
    checked_copy = checked_boxes[:] # Copy the list of checked boxes
    checked_copy.insert(0, checked_boxes[0])
    existent_folders = folders_exist(dest_dir)

    if all(existent_folders):
        return


    for i in range(7):
        if checked_copy[i] == existent_folders[i] and existent_folders[i]:
            checked_copy[i] = False

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
            if checked_copy[0]: # Checked_copy stores bool values
                globals()[variable] = path
                checked_copy.pop(0)
                folders.append(globals()[variable])
                print(f"Folder to create: {folders}")
            else:
                checked_copy.pop(0)
        
        folders.append(os.path.join(dest_dir, "Other")) # default destination dir
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
            ("Zips", "zips", zips),
            ("Documents", "documents", documents),
            ("Codes", "codes", codes),
            ("3D","threeD", threeD),
            ("Applications", "applications", applications),
    ]

    for folder in os.listdir(dest_dir):
        # print(folder)
        if folder == "Gallery":
            conc_dest_dir = os.path.join(dest_dir, folder)
            for sub_folder in os.listdir(conc_dest_dir):
                category = extension = sub_folder.lower()
                # print(category)
                globals()["dest_" + category] = os.path.join(dest_dir, folder, sub_folder)
                file_types.update({category: globals()[extension]})

        for folder_name, category, extension in file_types_attributes: 
            if folder == folder_name:
                globals()["dest_" + category] = os.path.join(dest_dir, folder)
                file_types.update({category: extension})
        
    # print(file_types)

# dest_folders_list(r"C:/Testing/Destination")

            # ("Gallery","photos", photos),
            # ("Gallery", "videos", videos),




def move_files(dest_dir: str):
    """
    Moves files from the source to the destination folders,
    sorting them based on their extensions.
    dest_dir: Destination directory path
    """
    existent_folders = folders_exist(dest_dir)
    if not any(existent_folders):
        return False

    dest_folders_list(dest_dir)
    print(f"File types: {file_types}")

    folder_other_exists = "Other" in os.listdir(dest_dir) # bool check whether Other exists

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
                    print(destination_path, file_path)
    else:
        return False

    return True



# TODO - Do not allow to run create folders whenever they had already been defined before.
# TODO - Add Copy suffix if file already exists; - Add progress bar; - Add skipping of corrupted files; - Check space in the dest to src to be able to move sufficiently;
# TODO - ADD configuration options (User would be able to chose their own); - Add logs for user understanding and further debugging
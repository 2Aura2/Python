import os
path ="AppData\\Local\\Temp"
folder_path = os.path.join(os.path.expanduser("~"), path)

# loop over all the files and directories in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            # remove the file
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            # remove the directory and all its contents
            os.rmdir(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path} with error {e}")




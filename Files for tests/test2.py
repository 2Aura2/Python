

import os

root_dir = "E:\\SteamLibrary" # change this to the drive letter you want to search

for dir_name, subdir_list, file_list in os.walk(root_dir):
    print(dir_name)
    for file_name in file_list:
        print(f"\t{file_name}")
        file_path = file_name
        length = str(len(file_path)).zfill(10)
        data = length+file_name
        print(data)


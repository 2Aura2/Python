

import os

root_dir = "E:/" # change this to the drive letter you want to search

for dir_name, subdir_list, file_list in os.walk(root_dir):
    print(dir_name)
    for file_name in file_list:
        print(f"\t{file_name}")


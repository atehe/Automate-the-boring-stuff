#! usr/bin/python3
# script to rename files and folder in directory to snake case

import os
from pathlib import Path


def rename_snake_case(path):
    for folder, subfolders, files in os.walk(path):
        if ".git" in folder:
            continue

        for file in files:
            file_snakecase = "_".join(file.split(" "))
            old_filepath = os.path.join(folder, file)
            new_filepath = os.path.join(folder, file_snakecase)

            print(f"renaming {old_filepath} to {new_filepath}")
            os.rename(old_filepath, new_filepath)

        for subfolder in subfolders:
            subfolder_snakecase = "_".join(subfolder.split(" "))
            old_path = os.path.join(folder, subfolder)
            new_path = os.path.join(folder, subfolder_snakecase)

            print(f"renaming {old_path} to {new_path}")
            os.rename(old_path, new_path)


rename_snake_case(os.getcwd())

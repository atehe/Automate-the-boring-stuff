#! usr/bin/python3
# rename_snake_case.py - rename files and folder in directory to snake case

import os


def rename_snake_case(path):
    for folder, subfolders, files in os.walk(path):
        if ".git" in folder:
            continue

        for file in files:
            file_snakecase = file.replace(" ", "_")
            old_filepath = os.path.join(folder, file)
            new_filepath = os.path.join(folder, file_snakecase)

            print(f"Renaming file: {file} to {file_snakecase}..")
            os.rename(old_filepath, new_filepath)

        for subfolder in subfolders:
            if subfolder == ".git":
                continue
            subfolder_snakecase = subfolder.replace(" ", "_")
            old_path = os.path.join(folder, subfolder)
            new_path = os.path.join(folder, subfolder_snakecase)

            print(f"Renaming folder:{subfolder} to {subfolder_snakecase}...")
            os.rename(old_path, new_path)


rename_snake_case(os.getcwd())

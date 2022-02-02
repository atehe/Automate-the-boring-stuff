from pathlib import Path
import os, shutil


def selective_copy(src_folder, dest_folder, ext):
    """Copies all file with a certain file exteension from one folder to another"""

    src_folder = str(Path(src_folder))
    dest_folder = str(Path(dest_folder))
    ext = ext.strip()

    for folder, _, files in os.walk(src_folder):
        for file in files:
            if file.endswith(ext):
                file_path = os.path.join(folder, file)
                print(f"Moving {file}: from {file_path} to {dest_folder} ..")
                shutil.move(file_path, dest_folder)

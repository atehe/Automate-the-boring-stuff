import os
from pathlib import Path

cwd = Path.cwd()

for i in range(15):
    folders = os.listdir(cwd)
    new_folder = "chapter_" + str(i)
    if new_folder not in folders:
        print(f"Creating {cwd }/{new_folder}")
        os.makedirs(cwd / new_folder)

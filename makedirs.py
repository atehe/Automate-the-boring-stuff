

import os
from pathlib import Path

cwd = Path.cwd()

for i in range(12):
    folders = os.listdir(cwd)
    new_folder = 'chapter ' + str(i)
    if not new_folder in folders:
        #print(cwd / new_folder)
        os.makedirs(cwd / new_folder)

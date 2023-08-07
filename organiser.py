import os
import shutil

from_dir = "images"
to_dir = "organised images"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,ext = os.path.splitext(file)
    print(name,ext)
    if ext == "":
        continue
    if ext in [".gif",".png",".jpg",".jfif"]:
        path1 = from_dir + "/" + file
        path2 = to_dir + "/" + ext
        path3 = to_dir + "/" + ext + "/" + file
        print(path3)
        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)
    
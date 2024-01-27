import sys
import os

files = os.listdir()

for f in files[1:]:
    file_name, file_extention = os.path.splitext(f)
    file_name = file_name[3:]
    new_name = f"{file_name}.csv"
    print(new_name)
    os.rename(f,new_name)
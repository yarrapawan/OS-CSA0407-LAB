# File Copying

import shutil
import os

# Source folder (the folder you want to copy)
src_folder = r"C:\Users\Dell\Desktop\New folder"

# Destination folder (the new copy location)
dst_folder = r"C:\Users\Dell\Desktop\y.txt"

try:
        # Copy entire folder including all files and subfolders
        shutil.copytree(src_folder, dst_folder)
        print(f"Folder copied successfully from:\n{src_folder}\n to\n{dst_folder}")

        # Show contents of the copied folder
        print("\nFiles in destination folder:")
        for root, dirs, files in os.walk(dst_folder):
            for file in files:
                print(os.path.join(root, file))
except Exception as e:
    print("Error:", e)
    

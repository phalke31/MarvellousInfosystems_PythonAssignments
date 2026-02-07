"""1. Design automation script which accepts directory name and displays checksum of all files.
Usage:  
DirectoryChecksum.py "Demo"

Demo is name of directory."""

import os
import hashlib # hashlib is used to create hashes/checksums for files (like MD5, SHA1).

folder = input("Enter folder name: ")

# Check if folder exists
if not os.path.exists(folder):
    print("Folder does not exist!")
else:
    # Walk through all folders and files
    for current_folder, subfolders, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(current_folder, file)  # full path -- os.path.join combines the folder path + file name

            # Open file in binary mode and calculate md5 checksum
            with open(file_path, "rb") as f:# f is alias
                data = f.read()
                checksum = hashlib.md5(data).hexdigest()

            # Print full file path and its checksum
            print(f"{file_path} = {checksum}")

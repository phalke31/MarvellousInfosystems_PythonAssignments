"""2. Design automation script which accepts directory name and writes names of duplicate files from that
directory into log file named as Log.txt. . Log.txt  file should be created into current directory.

Usage:  
DirectoryDuplicate.py "Demo"

Demo is name of directory."""

import os
import hashlib

# Ask user for folder name
folder = input("Enter folder name: ")

# Check if folder exists
if not os.path.exists(folder):
    print("Folder doesn't exist")
else:
    # Dictionary to store file checksums
    file_hashes = {}  # key = checksum, value = list of files with that checksum
    duplicates = []   # list to store duplicate file names

    # Loop through all files in the folder
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        # Only process files, not folders
        if os.path.isfile(file_path):
            # Open file in binary mode and calculate MD5 checksum
            with open(file_path, "rb") as f:
                data = f.read()
                checksum = hashlib.md5(data).hexdigest()

            # Check for duplicates
            if checksum in file_hashes:
                # Already exists -- this file is duplicate
                duplicates.append(file_path)
            else:
                # New file -- store its checksum
                file_hashes[checksum] = file_path

    # Write duplicates to Log.txt in current directory
    if duplicates:
        with open("Log.txt", "w") as log_file:
            for dup in duplicates:
                log_file.write(dup + "\n")
        print(f"Duplicate files written to Log.txt")
    else:
        print("No duplicate files found!")
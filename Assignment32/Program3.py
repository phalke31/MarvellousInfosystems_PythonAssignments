"""3. Design automation script which accepts directory name and deletes all duplicate files from that directory.
Write names of duplicate files from that directory into log1 file named as Log1.txt. . Log1.txt  file should be created
into current directory.

Usage:  
DirectoryDuplicateRemoval.py "Demo1"

Demo1 is name of directory."""

"""Input : python program3.py Demo1 """

import os
import sys
import hashlib

# Function to calculate file hash
def Directory_scanner(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()


# Main function
def main():

    # Check command line input
    if len(sys.argv) != 2:
        print("Usage: python program.py FolderName")
        return

    folder = sys.argv[1]

    # Check if folder exists
    if not os.path.isdir(folder):
        print("Folder not found")
        return

    files_data = {}   # Store hash and file path
    log = open("Log1.txt", "w")
    count = 0

    # Walk through directory
    for root, dirs, files in os.walk(folder):
        for name in files:

            path = os.path.join(root, name)

            file_hash = Directory_scanner(path)

            # Check for duplicate
            if file_hash in files_data:
                os.remove(path)
                log.write("Deleted: " + path + "\n")
                count += 1
            else:
                files_data[file_hash] = path

    log.close()

    # Final message
    if count == 0:
        print("No duplicate files found.")
    else:
        print(f"{count} duplicate files deleted. Check Log1.txt")

if __name__ == "__main__":
    main()

"""
print("----------------By takig input from user----------------------------")

import os
import hashlib

folder = input("Enter folder name: ")

if not os.path.exists(folder):
    print("Folder not found")
else:
    files_data = {}     # store file data
    log = open("Log1.txt", "w")
    count = 0

    for root, dirs, files in os.walk(folder):
        for name in files:

            path = os.path.join(root, name)

            with open(path, "rb") as f:
                data = f.read()

            file_hash = hashlib.md5(data).hexdigest()

            if file_hash in files_data:
                os.remove(path)
                log.write("Deleted: " + path + "\n")
                count += 1
            else:
                files_data[file_hash] = path

    log.close()

    if count == 0:
        print("No duplicate files found.")
    else:
        print("Duplicate files deleted. Check Log1.txt") """
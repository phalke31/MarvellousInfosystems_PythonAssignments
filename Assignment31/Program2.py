"""2. Design automation script which accepts directory name and two file extensions from user.
Rename all files with first file extension with the second file extension.

Usage:  
DirectoryRename.py "Demo1" ".txt" ".doc"

Demo1 is name of directory and .txt is the extension that we want to search and rename with .doc.
After execution this script each .txt file gets renamed as .doc."""

import sys
import os

def Search(DirName, OldExt, NewExt):

    if not os.path.exists(DirName):
        print("No such directory")
        return

    if not os.path.isdir(DirName):
        print("It's not directory")
        return

    for folder, subfolder, file in os.walk(DirName): # Outer loop → goes through all folders (folder by folder)
        for fname in file: # Inner loop → goes through all files inside each folder
            if fname.endswith(OldExt): # Only took files that end with the old extension (like .txt)
                
                # create old path coz os.rename() needs it 
                old_path = os.path.join(folder, fname) # Combines folder path + filename -- "Demo1/file1.txt"

                # creates new path
                new_fname = fname.replace(OldExt, NewExt) # Replaces the old extension with the new one - .txt --> .doc
                new_path = os.path.join(folder, new_fname) # file1.txt -->  file1.doc

                os.rename(old_path, new_path) # Renames the file on disk --> old to new
                print(f"Renamed {fname} with {new_fname}")           

def main():
    if len(sys.argv) != 4:
        print("Enter Directoryname and old and new extension as input in command line")
        return

    Search(sys.argv[1], sys.argv[2], sys.argv[3]) #Pass arguments

if __name__ == "__main__":
    main()
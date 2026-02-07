# used directory -- demo and temp 

"""3. Design automation script which accepts two directory names. Copy all files from first directory into
second directory. Second directory should be created at run time.

Usage:  
DirectoryCopy.py "Demo" "Temp"

Demo is name of directory which is existing and contains files in it.
We have to create new directory as Temp and copy all files from Demo to Temp."""

import sys
import os
import shutil # Copying files

def Copy_directory(src_dir, dest_dir):

    if not os.path.exists(src_dir):
        print(f"Source directory does not exist: {src_dir}")
        return
    
    # taken as below bcoz we need to create this directory at runtime if its already there then it will give an error
    if os.path.exists(dest_dir):
        print(f"Destination directory already exists: {dest_dir}")
        return
    
    # Copy entire directory (including subfolders and files)
    shutil.copytree(src_dir, dest_dir)
    print(f"Copied entire directory '{src_dir}' to '{dest_dir}' successfully!")
    
def main():
    
    if len(sys.argv) != 3:
        print("Enter Directorynames : src_dir and dest_dir")
        return

    Copy_directory(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
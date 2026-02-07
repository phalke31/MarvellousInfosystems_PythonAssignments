"""4. Design automation script which accepts two directory names and one file extension. Copy all files with 
the specified extension from first directory into second directory. Second directory should be created at run time.

Usage:  
DirectoryCopyExt.py "Demo" "Temp11" ".exe"

Demo is name of directory which is existing and contains files in it.
We have to create new directory as Temp1 and copy all files with extension .exe from Demo to Temp1."""

import sys
import os
import shutil

def copy_directory(src_dir, dest_dir, Extension):

    if not os.path.exists(src_dir):
        print(f"Source directory doesn't exists {src_dir}")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Destination folder/directory created: {dest_dir}")
    else:
        print(f"Destination folder/directory already exists: {dest_dir}")
        return
    
    for file in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, file)
        
        # Check if it is a file and has the given extension
        if os.path.isfile(src_file_path) and file.endswith(Extension):
            dest_file_path = os.path.join(dest_dir, file)
            shutil.copy2(src_file_path, dest_file_path)
            print(f"Copied: {file}")
    
def main():
    if len(sys.argv) != 4:
        print("Enter Directorynames src_dir and dest_dir and extension also")
        return

    copy_directory(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()

"""Why Copy2 : Using copy2 ensures the file keeps its original date/time and attributes, which is often important 
for executables.

If we use just copy, the file is copied, but its “modified date” will be set to now, which might not be desired."""


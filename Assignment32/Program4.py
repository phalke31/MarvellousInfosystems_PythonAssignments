
"""4. Design automation script which accepts directory name and deletes all duplicate files from that directory.
Write names of duplicate files from that directory into log file named as Log.txt. . Log.txt  file should be created into 
current directory. Display execution time required for the script.

Usage:  
DirectoryDuplicateRemoval.py "Demo2"

Demo2 is name of directory."""

import os
import sys
import hashlib
import time

# Function to calculate file hash
def Directory_scanner(filepath):

    timestamp = time.ctime()

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
    
    start_time = time.time() # start time 

    files_data = {}   # Store hash and file path
    log = open("Log.txt", "w")
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

    end_time = time.time() # end time

    # Final message
    if count == 0:
        print("No duplicate files found.")
    else:
        print(f"{count} duplicate files deleted. Check Log.txt")

    print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()


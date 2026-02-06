# Used demo folder :

"""1. Design automation script which accepts directory name and file extension from user. Display all files
with that extension.

Usage:  
DirectoryFileSearch.py "Demo" ".txt"

Demo is name of directory and .txt is the extension that we want to search."""


import sys
import os

def DirectoryFileSearch(DirName, Extension): 

    if not os.path.exists(DirName): # Checks : Does path exist?
        print("There is no such directory")
        return

    if not os.path.isdir(DirName): # Checks : Is it really a folder? -- sometimes user pass filenames
        print("It is not a directory")
        return

    for FolderName, SubFolder, FileNames in os.walk(DirName):
        for fname in FileNames:
            if fname.lower().endswith(Extension.lower()):
                print(fname)

def main():

    if(len(sys.argv) != 3): # if len(sys.argv) < 3 
        print ("Please provide directory and extension") # print("Usage : DirectoryFileSearch.py <DirectoryName> <Extension>")
        return
    
    DirectoryFileSearch(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

""" Input : python program1.py demo .txt
    Output :
        A.txt
        B.txt """
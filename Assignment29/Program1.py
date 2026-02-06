"""1: Check File Exists in Current Directory
Problem Statement:  
Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

Input:  
Demo.txt
Expected Output:  
Display whether Demo.txt  exists or not."""

import os

print("Current Directory:", os.getcwd()) # Current Directory: C:\Users\USER\Desktop\MarvellousInfosystem

Filename = input("Enter file name : ")

if os.path.exists(Filename):
    print(f"file: {Filename} exists in current directory")
else:
    print(f"file: {Filename} doesn't exists in current directory")
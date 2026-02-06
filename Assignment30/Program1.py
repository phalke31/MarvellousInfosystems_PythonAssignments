"""1. Count Lines in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input:
Demo.txt

Expected Output:
Total number of lines in Demo.txt."""

Filename = input("Enter filename: ")

try:
    fobj = open(Filename, "r")

    Count_lines = 0    # variable to store number of lines

    for line in fobj:
        Count_lines += 1

    print("Count of lines is : ", Count_lines)

    fobj.close()


except FileNotFoundError:
    print("File doesn't exist")
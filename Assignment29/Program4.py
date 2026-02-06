"""4: Compare Two Files (Command Line)
Problem Statement:  
Write a program which accepts two file names through command line arguments and compares the contents of both files.

If both files contain the same contents, display Success

Otherwise display Failure

Input (Command Line):  
Demo.txt  Hello.txt

Expected Output:  
Success OR Failure"""

import sys

try:
    Filename1 = sys.argv[1] # file1 took as input vi cmdline
    Filename2 = sys.argv[2] # file2 took as input vi cmdline

    f1 = open(Filename1, "r") # open data 
    f2 = open(Filename2, "r")

    if f1.read() == f2.read(): # read and compare data of file
        print("Success")
    else:
        print("Failure")

except FileNotFoundError:
    print("One of the file doesn't exists")


 


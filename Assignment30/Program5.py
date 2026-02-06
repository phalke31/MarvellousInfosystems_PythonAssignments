"""5: Search a Word in File
Problem Statement:  
Write a program which accepts a file name and a word from the user and checks whether that word is present in the 
file or not.

Input:  
Demo.txt  Marvellous

Expected Output:  
Display whether the word Marvellous is found in Demo.txt  or not."""

Filename = input("Enter filename : ")
Word = input("Enter word need to be find from file : ")

try:
    fobj = open(Filename, "r")
    data = fobj.read()

    if Word.lower() in data.lower():
        print("Word found")
    else:
        print("Word not found ")
    
    fobj.close()

except FileNotFoundError:
    print("File doesn't exists")
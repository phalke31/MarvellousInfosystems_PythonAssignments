"""2: Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file.

Input:
Demo.txt

Expected Output:
Total number of words in Demo.txt."""

Filename = input("Enter name : ")

try:
    fobj = open(Filename, "r")

    count_words = 0

    for line in fobj:
        words = line.split() # Break the line into words using split()
        # print(len(words)) 

        count_words += len(words)
    
    print("Count of words is : ",count_words )

except FileNotFoundError:
    print("File doesn't exist")
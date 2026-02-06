"""5: Frequency of a String in File -- Demo3.txt used here
Problem Statement:  
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) 
of that string in the file.

Input:  
Demo.txt  Marvellous

Expected Output:  
Count how many times "Marvellous" appears in Demo.txt."""

import sys

Filename = sys.argv[1] # take file input

string_search = sys.argv[2]

fobj = open(Filename, "r") # open file in read mode
data = fobj.read() # here we read all the content of file (Demo3.txt)

count = data.count(string_search)

fobj.close()
print("Count of string ",string_search, "is", count)



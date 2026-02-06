"""2: Display File Contents
Problem Statement:  
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

Input:  
Demo.txt

Expected Output:  
Display contents of Demo.txt  on console."""

# Filename = input("Enter file name: ")
# fobj = open(Filename, "r")
# data = fobj.read()
# print(data)

# By using exception handling 

Filename = input("Enter filename : ")

try:
    fobj = open(Filename, "r")  # open file in read mode
    data = fobj.read() # read the file
    print("File gets successfully exicuted : ")
    print(data)   # display content if file exists 

    fobj.close() # close file

except FileNotFoundError: # Handle known errors specifically, unknown errors generally hence used =-- FileNotFoundError
    print("File is not present in such directory")

# except Exception as e:
#     print("Other error:", e) # If file doesn't exist : Other error: [Errno 2] No such file or directory: 'shreya.txt'

""" except Exception as e

 Handles any other unexpected error.
 e stores the error message. """

""" Exception word catches any error like below :
File not found
Division by zero
Wrong data type
Index error
Value error """

"""
FileNotFoundError (Specific Error)
This error happens only when file does not exist. -- and it catches only that error
"""
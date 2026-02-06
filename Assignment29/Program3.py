"""3: Copy File Contents into a New File (Command Line)
Problem Statement:  
Write a program which accepts an existing file name through command line arguments, creates a new file named Demo1.txt,
and copies all contents from the given file into Demo.txt..

Input (Command Line):  
ABC.txt

Expected Output:  
Create Demo1.txt  and copy contents of ABC.txt  into Demo1.txt.."""

import sys

filename = sys.argv[1] # it will take existing file as input via cmd line 
existing_file = open(filename, "r") # Open the given file in read mode

data = existing_file.read() # read the data of existing file 

new_file = open("Demo1.txt", "w")

new_file.write(data) # it will write the data in newly created file

# close boh files
existing_file.close()
new_file.close()

print("Existing file : ABC.txt data copied successfully into Demo1.txt")


# Taking input from user with exception handling :

# import sys

# try :
#     Filename = input("Enter existing file name : ")

#     exisiting_file = open(Filename, "r") # open existing file 
#     data = exisiting_file.read() # read the existing file 

#     new_file = open("Demo2.txt", "w") # new file created here in write mode 
#     new_file.write(data) # it will store of (data) inside new file 

#     exisiting_file.close()
#     new_file.close()

#     print("Copied data successfully in new file")

# except FileNotFoundError:
#     print("File doesn't exist")


"""3: Display File Line by Line
Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

Input:
Demo.txt

Expected Output:
Display each line of Demo.txt one by one."""

# Read line by line data :

Filename = input("Enter filename : ")

try :
    fobj = open(Filename, "r")

    for line in fobj:
        print(line, end="") # end="" avoids extra blank line

    fobj.close()

except FileNotFoundError:
    print("File doesn't exists")

# Read whole data of file at once : 
# Filename = input("Enter filename : ")

# try:
#     fobj = open(Filename, "r")
#     data = fobj.read()

#     print(data)


# except FileNotFoundError:
#     print("File doesn't exists")
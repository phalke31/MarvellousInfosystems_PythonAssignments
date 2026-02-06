"""4: Copy File Contents into Another File
Problem Statement:  
Write a program which accepts two file names from the user.

First file is an existing file

Second file is a new file

Copy all contents from the first file into the second file.

Input:  
ABC.txt  Demo.txt

Expected Output:  
Contents of ABC.txt  copied into Demo.txt"""

Filename1 = input("Enter existing filename : ")
Filename2 = input("Enter new filename : ")

try:
    F1 = open(Filename1, "r")
    data = F1.read() # read data from F1

    F2 = open(Filename2, "w")
    F2.write(data) # write data in new line by using this line

    print("Data copied successfully")

    F1.close()
    F2.close()


except FileNotFoundError:
    print("File doesn't exists")
"""4. Write a program which accepts one number and prints binary equivalent."""

num = int(input("Enter a number: "))
print("Binary equivalent:", bin(num)[2:]) #bin(num) -- it will share binary number in format ob1101 : [2:] -- it's indexing start from 2 so it will print the numbr from index[2] = 1101
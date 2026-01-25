""" Write a program which accepts one number and checks whether it is palindrome or not.
Input: 121
Output: Palindrome """

Number = input("Enter number : ")

if Number == Number[::-1]: 
    print("Number is palindrome")
else:
    print("Number is not palindrome")

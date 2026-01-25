""" Write a program which accepts one number and prints all even numbers till that number.

Input: 10
Output: 2 4 6 8 10 """

Number = int(input("Enter number : "))

for i in range(2, Number+1, 2):
    print(i)


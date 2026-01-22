""" Write a program which accepts one number and prints its factors.
Input: 12
Output: 1 2 3 4 6 12
"""

Number = int(input("Enter Number : "))

for i in range(1, Number+1):
    if Number % i == 0:
        print(i)
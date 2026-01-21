""" 3. Write a program which accepts one number and prints sum of digits.
Input: 123
Output: 6
"""

Number = int(input("Enter Number : "))
Sum = 0
i = 1

while i <= Number:
    Sum = Sum + i
    i += 1

print("Sum of given number is : ", Sum)




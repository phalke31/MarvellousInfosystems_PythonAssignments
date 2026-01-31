"""Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
Input:
Number of elements: 7
Input Elements: 13 5 45 7 4 56 34
Output: 56"""

Numbers = list(map(int, input("Enter numbers: ").split()))
Maximum_Number = max(Numbers)

print("Maximum number is : ", Maximum_Number)



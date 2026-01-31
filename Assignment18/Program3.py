"""3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
Input:
Number of elements: 4
Input Elements: 13 5 45 7
Output: 5"""

Numbers = list(map(int, input("Enter elements : ").split()))
Minimum_Number = min(Numbers)
print("Minimum number is : ", Minimum_Number)
"""4. Write a program which accept N numbers from user and store it into List. Accept one another number from user 
and return frequency of that number from List.

Input:
Number of elements: 11
Input Elements: 13 5 45 7 4 56 5 34 2 5 65
Element to search: 5
Output: 3"""

Numbers = list(map(int, input("Enter elements : ").split()))
No = int(input("Enter element for which you want frequncy : ")) # No for which we want count

Frequency = Numbers.count(No) # to find count of that element
print("Frequency of ", No, "is : ", Frequency)




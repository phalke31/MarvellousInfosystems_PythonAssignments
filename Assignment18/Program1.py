"""Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130"""

Numbers = list(map(int, input("Enter numbers: ").split()))
total = sum(Numbers)
print("Sum of all elements:", total)



# .split() → separates them into ['13','5','45','7','4','56']
# map(int, ...) → converts to [13,5,45,7,4,56]






    

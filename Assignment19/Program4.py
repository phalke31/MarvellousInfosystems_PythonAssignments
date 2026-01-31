"""4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list
 of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which
   are even. Map function will calculate its square. Reduce will return addition of all that numbers.  

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204"""

from functools import reduce  

numbers = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

# filter
filtered_list = list(filter(lambda x: x % 2 == 0, numbers))
print("List after filter:", filtered_list)

# map
square_of_filtered_list = list(map(lambda x: x ** 2, filtered_list))
print("List after map:", square_of_filtered_list)

# reduce
Addition_of_squares = reduce(lambda x, y: x + y, square_of_filtered_list)
print("Output of reduce:", Addition_of_squares)
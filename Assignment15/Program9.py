"""9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements."""

from functools import reduce

Numbers = [1,2,3,4,5,6]

Data_after_reduce = reduce(lambda a, b: a*b, Numbers)
print(Data_after_reduce)
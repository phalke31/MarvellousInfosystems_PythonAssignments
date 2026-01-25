"""4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements."""

from functools import reduce

Number = [1,2,3,4,5]

Sum =  reduce(lambda x, y : x + y , Number)
print(Sum)

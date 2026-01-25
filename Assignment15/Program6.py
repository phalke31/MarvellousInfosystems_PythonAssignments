"""6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element."""

from functools import reduce

Number = [1,2,3,4,5]

Minimum_Number = reduce(lambda x,y : x if x<y else y, Number)
print("Minimum number is : ", Minimum_Number)
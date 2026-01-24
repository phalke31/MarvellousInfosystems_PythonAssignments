"""5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element."""
from functools import reduce

Number = [1,2,3,4,5]

Maximum_Number = reduce(lambda x,y : x if x>y else y, Number)
print("Maximum number is : ", Maximum_Number)
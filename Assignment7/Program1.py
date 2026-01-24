"""1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number."""

# 1)
Number = [1,2,3,4,5]

Data = list(map(lambda a : a * a, Number))
print(Data)

# 2)

Number = [6,7,8]

Data = map(lambda a : a * a, Number)
print(list(Data))
      

print("---------Without using list--------------------")

# Number = [1, 2, 3, 4, 5]

# Data = map(lambda a: a * a, Number)

# for item in Data:
#     print(item, end= " ")
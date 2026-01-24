"""7. Write a lambda function which accepts one number and returns True if divisible by 5"""

a = int(input("Enter Number : "))

Result = lambda a : True if (a % 5 == 0) else False
print(Result(a))
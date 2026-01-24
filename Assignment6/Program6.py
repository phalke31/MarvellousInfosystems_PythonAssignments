"""6. Write a lambda function which accepts one number and returns True if number is odd otherwise False."""

a = int(input("Enter number : "))

Result = lambda a : True if (a % 2 != 0) else False
print(Result(a))
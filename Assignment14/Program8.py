"""8. Write a lambda function which accepts two numbers and returns addition."""

a = int(input("Enter Number: "))
b = int(input("Enter Number: "))

Result = lambda a, b : (a + b)
print(Result(a, b))
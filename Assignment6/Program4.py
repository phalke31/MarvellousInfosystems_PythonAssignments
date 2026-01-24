"""4. Write a lambda function which accepts two numbers and returns minimum number."""

# a = int(input("Enetr first number : "))
# b = int(input("Enetr second number : "))

# Minimum_Number = lambda a, b : a if a < b else b
# print(Minimum_Number(a,b))


a = int(input("Enetr first number : "))
b = int(input("Enetr second number : "))

Minimum_Number = lambda a, b : ("a",a) if a < b else ("b",b)
print(Minimum_Number(a,b))
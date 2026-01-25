"""10. Write a lambda function which accepts three numbers and returns largest number."""

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

Largest_number = lambda a, b, c : a if (a>b and a>c) else b if (b>a and b>c) else c
print(Largest_number(a,b,c))
"""Write a lambda function which accepts one number and returns cube of that number."""

Cube = lambda a : a*a*a
print(Cube(2))

print("-------------By taking input from user----------------")

a = int(input("Enter number : "))

Cube = lambda a : a*a*a
print(Cube(a))
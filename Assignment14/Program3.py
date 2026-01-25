"""3: Write a lambda function which accepts two numbers and returns maximum number."""

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

Maximun_Number = lambda a, b : a if a > b else b # value_if_true if condition else value_if_false
print(Maximun_Number(a, b))
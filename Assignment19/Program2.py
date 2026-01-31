"""2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.  
Input : 4   3
Output : 12
Input : 6   3
Output : 18"""

a = int(input("Enter Number1 : "))
b = int(input("Enter Number2 : "))

Multiplication = lambda a,b : a*b

print("Multiplication is : ", Multiplication(a,b))
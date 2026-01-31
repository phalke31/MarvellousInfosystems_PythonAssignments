"""1.Create one module named as Arithmetic which contains functions as Add() for addition, Sub() for subtraction, 
Mult() for multiplication and Div() for division. All functions accept two parameters as number and perform the
 operation. Write python program which call all the functions from Arithmetic module by accepting the parameters from 
 user."""


import Arithmatic_program1

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

print(Arithmatic_program1.Add(No1, No2))
print(Arithmatic_program1.Sub(No1, No2))
print(Arithmatic_program1.Mul(No1, No2))
print(Arithmatic_program1.Div(No1, No2)) 

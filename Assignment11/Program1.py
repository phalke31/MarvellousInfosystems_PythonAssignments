""" 1. Write a program which accepts one number and checks whether it is prime or not.
Input: 11
Output: Prime Number """

Number = int(input("Enter Number : "))

if Number <= 1:
    print("Its not a prime number")
else :
    for i in range(2, Number):
        if(Number % i == 0):
            print("Its not a prime number")
            break
    else:
        print("It's prime number")


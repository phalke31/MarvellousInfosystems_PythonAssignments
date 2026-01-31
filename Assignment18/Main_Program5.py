"""5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers
 from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is 
 part of our user-defined module named as MarvellousNum. Name of the function from main python file should be 
 ListPrime().

Input:
Number of elements: 11"""

import MarvellousNum  # Import your module

def ListPrime():
    numbers = list(map(int, input("Enter numbers: ").split()))
    total = 0

    for num in numbers:
        if MarvellousNum.chkprime(num):
            total += num
    print("Sum of prime numbers:", total)

ListPrime()
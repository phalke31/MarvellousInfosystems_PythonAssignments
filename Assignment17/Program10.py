"""10. 10. Write a program which accept number from user and return addition of digits in that number.
Input : 518794
Output : 37"""

Number = int(input("Enter Number : "))

def Addition_of_digit(Number):
    total = 0
    
    while Number > 0:
        digit = Number % 10
        total = total + digit # Add last digit to total
        Number = Number // 10 # Remove last digit
    return total

print(Addition_of_digit(Number))




    
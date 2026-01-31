"""9. Write a program which accept number from user and return number of digits in that number.
Input : 5187934
Output : 7"""

Number = int(input("Enter Number : "))

def digits_in_number(Number):
    if Number == 0:
        return 1
    
    count = 0

    while Number > 0:
        Number = Number // 10
        count += 1
    return count

    
print(digits_in_number(Number))









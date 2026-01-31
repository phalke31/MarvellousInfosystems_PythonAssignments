"""4. Write a program which accept one number from user and return addition of its factors.
Input : 12
Output : 16 (1 + 2 + 3 + 4 + 6)"""

Number = int(input("Enter Number : "))

def Addition():
    result = 0
    for i in range(1,Number):
        if (Number % i == 0):
            result = result + i
    return result

Ans = Addition()
print("Addition of factors is : ", Ans)
           
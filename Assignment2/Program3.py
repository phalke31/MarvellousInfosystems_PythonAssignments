""" Write a program which accepts one number and prints factorial of that number.
Input: 5
Output: 120 """

Number = int(input("Enetr number : "))
fact = 1

for i in range(1,Number+1):
    fact = fact * i
print("Factorial of given numer is : ", fact)





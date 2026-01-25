""" 2. Write a program which accepts one number and prints sum of first N natural numbers.
Input: 5
Output: 15 """

Number = int(input("Enter number : "))

sum = 0
i = 1

while(i <= Number):
    sum = sum + i
    i += 1

print("Sum of first", Number, "natural numbers =", sum)



 
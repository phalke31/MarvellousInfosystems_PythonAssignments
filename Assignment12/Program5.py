"""5. Write a program which accepts one number and prints that many numbers in reverse order.
Input: 5
Output: 5 4 3 2 1 """

Number = int(input("Enter number : "))

for i in range(Number, 0, -1):
    print(i)
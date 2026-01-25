"""4. Write a program which accepts one number and prints that many numbers starting from 1.
Input: 5
Output: 1 2 3 4 5 """

Number = int(input("Enter number : "))

for i in range(1, Number+1):
    print(i)
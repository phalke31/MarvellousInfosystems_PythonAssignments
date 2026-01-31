"""8. Write a program which accept one number and display below pattern.
Input : 5
Output :
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
"""

Number = int(input("Enter Number : "))

def display():
    for i in range(1, Number + 1):
        for j in range(1, i+1):
            print(j , end= " ")
        print()

display()




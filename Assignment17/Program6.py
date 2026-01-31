"""6. Write a program which accept one number and display below pattern.
Input : 5
Output :
*
*   *
*   *   *
*   *   *   *"""

Number = int(input("Enter Number : "))

def display():
    for i in range(1, Number ):
        print(i * "* " )
display()
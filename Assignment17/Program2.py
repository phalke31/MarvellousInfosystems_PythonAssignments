"""2. Write a program which accept one number and display below pattern.
Input : 5
Output :
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *"""


Number = int(input("Enter number : "))

def display():
    for i in range(1,Number + 1):
        print(Number * " * ")

display()
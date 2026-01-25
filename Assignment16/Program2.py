"""2. Write a program which contains one function named as ChkNum() which accepts one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.
Input : 11 ? Output : Odd Number
Input : 8 ? Output : Even Number"""

No = int(input("Enter number : "))

def chknum():
    if No%2 == 0:
        print("Even Number")
    else :
        print("Odd Number")

chknum()

# Without taking input from user just passing parameter inside function :

# def chknum (a):
#     if a%2 == 0:
#         print("Even Number")
#     else :
#         print("Odd Number")

# chknum(6)
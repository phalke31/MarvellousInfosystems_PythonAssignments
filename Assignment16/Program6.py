"""6. 
Write a program which accept number from user and check whether that number is positive or negative or zero.
Input : 11 ? Output : Positive Number
Input : -8 ? Output : Negative Number
Input : 0 ? Output : Zero"""

def chknum():

    No = int(input("Enetr number : "))
    if(No > 0):
        print("No is positive")
    elif(No<0):
        print("No is negative")
    else:
        print("Zero")

chknum()
""" 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5.
Input:
15
Output:
Divisible by 3 and 5 """

Number = int(input("Enter number = "))

def verify():
    if (Number % 3 == 0 and Number % 5 == 0):
        print("Number is divisible by 3 and 5")
    else :
        print("Number is not divisible by 3 and 5")
        
verify()

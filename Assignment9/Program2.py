""" 2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
Input:
10 20
Output:
20 is greater """

def CheckGreater(No1, No2):
    if (No1 > No2):
        print("No1 is greater : ", No1)
    else:
        print("No2 is greater : ", No2)

CheckGreater(12,13)
    
print("---------------By taking input from user----------------------------")

Number1 = int(input("Enetr first number : "))
Number2 = int(input("Enetr second number : "))

def ChkGreater():
    if (Number1 > Number2):
        print("Number1 is greater : ", Number1)
    else:
        print("Number2 is greater : ", Number2)
        
ChkGreater()
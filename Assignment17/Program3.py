"""3. Write a program which accept one number from user and return its factorial.
Input : 5
Output : 120 """

Number = int(input("Enter Number : "))

def Factorial():
    result = 1
    for i in range(1,Number+1):
        result = result*i
    print(result)

Factorial()

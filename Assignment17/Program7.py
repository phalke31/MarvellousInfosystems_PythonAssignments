"""7. Write a program which accept one number and display below pattern.
Input : 5
Output :
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5"""

# Number = int(input("Enter Number : "))

# def display():
#     for i in range(1, Number+1):
#         print("1 2 3 4 5 " * 1)

# display()


Number = int(input("Enter Number : "))

def display():
    for i in range(1, Number+1): # i treatd as rows 
        for j in range(1, Number+1):
            print(j, end= " ")
        print()  # new line after each row
    
display()

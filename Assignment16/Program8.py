""" 8. Write a program which accept number from user and print that number of “*” on screen.
Input : 5 ? Output : * * * * * """

# No = int(input("Enter number : "))
# print("*" * No)

# By using function 

def print_stars(No):
    print("*" * No)

No = int(input("Enter number : "))
print_stars(No)
"""5. Write a program which accept one number from user and check whether that number is Prime Number or not.
Input : 5
Output : It is Prime Number"""


Number = int(input("Enetr Number : "))

def chk_prime_or_not():
    if Number<=1:
        print("It's not prime number")
        return
    
    for i in range(2, Number):
        if Number % i == 0:
            print("It's not prime number")
            break
    else :
        print("It's prime number")

chk_prime_or_not()
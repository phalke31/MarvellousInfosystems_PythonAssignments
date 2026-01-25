""" 3. Write a program which accepts one number and checks whether it is perfect number or not.
Input: 6
Output: Perfect Number """ # Sum of factors = Number

Number = int(input("Enter number : "))

Sum = 0

for i in range(1, Number):
    if Number % i == 0:
        Sum += i

if Sum == Number: 
    print("Perfect Number")
else:
    print("Not a Perfect Number")
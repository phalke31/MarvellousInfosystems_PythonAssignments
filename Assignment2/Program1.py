"""" Write a program which accepts one number and prints multiplication table of that number.
Input: 4
Output:
4 8 12 16 20 24 28 32 36 402 """

Number = int(input("Enetr Number : "))

for i in range (1, 11):
    print(Number, "x", i, "=", Number * i)

print("------------By using while loop------------------------")

No = int(input("Enetr No : "))
i = 1

while (i<=10):
    print(No,"X", i,"=",No*i)
    i += 1
    



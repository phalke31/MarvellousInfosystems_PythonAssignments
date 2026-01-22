""" 5. Write a program which accepts marks and displays grade.
Condition Example:
≥ 75 → Distinction
≥ 60 → First Class
≥ 50 → Second Class
< 50 → Fail """

Marks = int(input("Enter Marks: "))

if Marks >= 75:
    print("Distinction")
elif Marks >= 60:
    print("First Class")
elif Marks >= 50:
    print("Second Class")
else:
    print("Fail")
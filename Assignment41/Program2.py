# Q3 : Use KNN to predict whether a student passes or fails based on study hours and attendance.

""" Dataset:

Study Hours	Attendance	Result
2	60	Fail
5	80	Pass
6	85	Pass
1	50	Fail """

import math

print("Step1 : Create Dataset")
dataset = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85,	"Pass"),
    (1,	50,	"Fail")
]
print(dataset)
print("Dataset created succefully")

Border = "_"*70
print(Border)

print("Step2 : Accept input from user study hours and attendance ")

Study_hrs = int(input("Enter study hours : "))
Attendace = int(input("Enter attendance : "))

print(Border)
print("Step3 : Create empty list to store distances")
distances = []

for data in dataset:
    hours = data[0]
    attend = data[1]
    result = data[2]

    distance = math.sqrt((Study_hrs - hours)**2 + (Attendace - attend)**2)

    print("Distances are : ", distance) # distance == measured by using (x-x1) and (y-y1)
    distances.append((distance,result))

print(Border)
print("Step4 : Sort distances (smallest first)")
distances.sort()  # distance is first value so while sorting it will take automatically distance

print("Sorted distances are : ", distances)

print(Border)
print("Step5 : Select K nearest neighbors")

k = 3 # look at the 3 nearest neighbours -- k should be odd then only we will get results
neighbours = distances[0:k]  # from distance it will take first 3 closest points

print("Nearest first 3 values are of k : ", neighbours)

print(Border)
print("Step6 : Major Voting")

# create counters first 
Pass_count = 0
Fail_count = 0

# (10.19, 'Pass') -- n[0] = 10.19 and n[1] = pass
for n in neighbours:
    if n[1] == "Pass":
        Pass_count += 1
    else:
        Fail_count += 1

print(Border)
print("Step7 : Predict the Student passed or failed")

if Pass_count > Fail_count:
    prediction = "Student Pass"
else:
    prediction = "Student Fail"

print("Prediction by voting majority : ", prediction)

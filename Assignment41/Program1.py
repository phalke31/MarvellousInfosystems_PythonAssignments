# Question 1:
""" 1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
 The algorithm should be implemented manually without using any machine learning library.

The program should:
Calculate Euclidean distance
Sort distances
Select K nearest neighbors
Predict the class based on majority voting

Dataset:

Point	X	Y	Label
A	1	2	Red
B	2	3	Red
C	3	1	Blue
D	6	5	Blue """

import math

print("Step1 : Create Dataset")
dataset = [
    ("A",1,	2, "Red"),
    ("B",2,	3, "Red"),
    ("C",3,	1, "Blue"),
    ("D",6,	5, "Blue")
]
print(dataset)
print("Dataset created succefully")

Border = "_"*70
print(Border)

print("Step2 : Accept X and Y coordinates of a new point from the user")

x = float(input("Enter X coordinate : "))
y = float(input("Enter Y coordinate : "))

print(Border)
print("Step3 : Create empty list to store distances")

distances = []

for point in dataset:
    name = point[0]
    x1 = point[1]
    y1 = point[2]
    label = point[3]

    distance = math.sqrt((x-x1)**2 + (y-y1)**2)

    print("Distances are : ", distance) # distance == measured by using (x-x1) and (y-y1)

    distances.append((name,distance,label))

print(Border)
print("Step4 : Sort distances (smallest first)")
distances.sort(key=lambda item: item[1])

print("Sorted distances are : ", distances)

print(Border)
print("Step5 : Select K nearest neighbors")

k = 3 # look at the 3 nearest neighbours -- k should be odd then only we will get results
neighbours = distances[0:k]  # from distance it will take first 3 closest points

print("Nearest first 3 values are of k : ", neighbours)

for n in neighbours:
    print(n[0], "- Distance:", round(n[1],2))
    
print(Border)
print("Step6 : Major Voting")

# create counters first 
Red = 0
Blue = 0

# ('A', 0.0, 'Red') -- n[0]=A , n[1]=0.0, n[2]=Red
for n in neighbours:
    if n[2] == "Red":
        Red += 1
    else:
        Blue += 1

print(Border)
print("Step7 : Predict the Class")

if Red > Blue:
    prediction = "Red"
else:
    prediction = "Blue"

print("Predicted class by voting majority : ", prediction)

# Question 2: 

print(Border)
print("Prediction Results for different K values [1,3,5]")

for k in [1,3,5]:  

    neighbours = distances[0:k]

    Red = 0
    Blue = 0

    # Majority Voting
    for n in neighbours:
        if n[2] == "Red":
            Red += 1
        else:
            Blue += 1

    # Prediction
    if Red > Blue:
        prediction = "Red"
    else:
        prediction = "Blue"

    print("K =",k,"→",prediction)

# Question 3 :


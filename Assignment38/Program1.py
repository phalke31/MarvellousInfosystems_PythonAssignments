"""1. Write a Python program to load the file student_performance_ml.csv using pandas and perform operations"""

import pandas as pd
from matplotlib import pyplot as plt

border = "-"*40
print(border)

print("1: Load the data")

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)
print("Dataset gets loaded successfully....")

print(border)

print(df.head()) # First 5 records
print(df.tail()) # Last 5 records
print(df.shape) # Total number of rows and columns
print(df.columns) # Total number of rows and columns
print(df.dtypes) # Data types of each column

print(border)
print("2 : Write a program to : ")
print(border)

total_students = len(df)
print("Total number of students:", total_students) # total no of student 

passed_students = (df["FinalResult"] == 1).sum() # Passed student count 
failed_students = (df["FinalResult"] == 0).sum() # Failed student count

print(border)
print("3 : Using pandas functions, calculate and display: ")
print(border)

avg_studyhrs = df["StudyHours"].mean()
print("Average Study Hours:", avg_studyhrs) # Avg study hrs

avg_attendance = df["Attendance"].mean()
print("Average Attendance:", avg_attendance) # Avg attendance

max_score = df["PreviousScore"].max()
print("Maximum Previous Score:", max_score) # max previous score

min_sleep = df["SleepHours"].min()
print("Minimum Sleep Hours:", min_sleep) # min sleep hrs 

print(border)
print("4 : Use value_counts() to analyze the distribution of FinalResult ")
print(border)

result_counts = df["FinalResult"].value_counts() # To count final result 

print("FinalResult is :", result_counts)

result_percentage = df["FinalResult"].value_counts(normalize=True) * 100 # To count percetage 
# result_percentage = (result_counts / len(df)) * 100
# (normalize=True)  : This gives RATIO (Proportion) not count 

print("percentages is : ", result_percentage)

"""The distribution shows how many students passed and failed.
If both classes are nearly equal, the dataset is balanced.
If one class is much higher, the dataset is imbalanced.

The dataset is balanced because the number of pass and fail students is nearly equal. 
There is no major difference between the two classes.

"""

print(border)
print("5 : Based on the dataset values, analyze whether: ")
print(border) # Analyze StudyHours & Attendance vs FinalResult

# Question 1 : Higher StudyHours increase the chance of passing

pass_avg_study = df[df["FinalResult"]==1]["StudyHours"].mean()
print("Average StudyHours of Passed students : ", pass_avg_study)

fail_avg_study = df[df["FinalResult"]==0]["StudyHours"].mean()
print("Average StudyHours of Failed students : ", fail_avg_study)

# Question 2 : Higher Attendance improves FinalResult

pass_avg_Attendance = df[df["FinalResult"]==1]["Attendance"].mean()
print("Average Attendance of pass students : ", pass_avg_Attendance)

fail_avg_Attendance = df[df["FinalResult"]==0]["Attendance"].mean()
print("Average attendance of fail students : ", fail_avg_Attendance)

""""Students who passed generally studied more hours.
Students with higher attendance mostly passed."""

print(border)
print("6 : Plot a histogram of StudyHours")
print(border) 

plt.figure(figsize=(7,5)) # standaed figure size (7,5) we can use other also
plt.hist(df["StudyHours"], bins=5) # If StudyHours values are from 1 to 10 == bins=5 → divide into 5 groups : It will decide particular range while plottong the graph 
plt.xlabel("Study hours") 
plt.ylabel("No of students")
plt.title("Distribution deails of study hours")
plt.show()

""""The histogram shows distribution of study hours.
It helps identify how many students study low, medium, or high hours.
Most students fall in the middle range, indicating average study habits."""

print(border)
print("7 : Create a scatter plot of StudyHours vs PreviousScore.")
print(border) 

plt.figure(figsize=(7,5))
plt.scatter(df["StudyHours"],df["PreviousScore"])
plt.xlabel("Study hours")
plt.ylabel("Previous score of students")
plt.title("Scatter plot of StudyHours vs PreviousScore")
plt.show()

"""The graph shows that students who study more hours usually get higher previous scores.
This means when study time increases, marks also increase.
So there is a good connection between studying and performance."""

print(border)
print("8 : Draw a boxplot for Attendance.Identify if any outliers are present" )
print(border) 

plt.figure(figsize=(6,5))

plt.boxplot(df["Attendance"])
plt.ylabel("Attendance")
plt.title("Boxplot of Attendance")
plt.show()

"""The boxplot shows the distribution of attendance among students.
The median attendance is around 80%, which means most students attend regularly.
Most attendance values lie between 70% and 89%.
The minimum attendance is around 60% and maximum is around 96%.
There are no outliers, which means there are no extreme attendance values.
Overall, attendance data is fairly consistent and well distributed."""

print(border)
print("9 : Create a plot showing relationship between AssignmentsCompleted and FinalResult." )
print(border) 

plt.figure(figsize=(7,5))

plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])
plt.xlabel("Assignments completed")
plt.ylabel("Final Result (0 = fail, 1 = pass)")
plt.show()

print(border)
print("10 : Plot SleepHours against FinalResult, Does sleeping more guarantee success? Explain" )
print(border)

"""Students who completed fewer assignments mostly failed.
Students who completed more assignments mostly passed.
This shows completing assignments increases chance of passing.
AssignmentsCompleted is an important factor."""

plt.figure(figsize=(7,5))

plt.scatter(df["SleepHours"], df["FinalResult"])
plt.xlabel("Sleep hours")
plt.ylabel("Final Result (0 = Fail, 1=Pass)")

plt.show()

"""Students with very low sleep mostly failed.
Students with moderate sleep mostly passed.
However, some students with similar sleep hours both passed and failed.
Therefore, sleeping more does not guarantee success.
Balanced study and sleep are important."""


# Final Overall Conclusion

"""From analysis:
StudyHours, Attendance, and AssignmentsCompleted strongly affect performance.
PreviousScore also influences final result.
SleepHours alone does not determine success"""




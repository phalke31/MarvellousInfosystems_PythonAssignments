"""Write a Python program that calculates the variance and standard deviation of the dataset:

[6, 7, 8, 9, 10, 11, 12]
Display both results."""

# Variance Formula :  Variance = average of (value − mean)²
# Standard Deviation Formula : Standard Deviation = √Variance

import numpy as np
Data = [6, 7, 8, 9, 10, 11, 12]

Mean = np.mean(Data)
print("Mean of data is : ", Mean)

total = 0

for i in Data:
    total = total + (i - Mean) ** 2 # total += (i - Mean) ** 2

Variance = total / len(Data)
print("Variance is : ", Variance)

Standard_Deviation = np.sqrt(Variance)
print("Standard Deviation is : ", Standard_Deviation)

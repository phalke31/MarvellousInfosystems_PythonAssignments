"""Write a Python program to calculate the Euclidean distance between two points before and 
after applying feature scaling, and explain the difference in results."""


Data =[[25, 20000],
[30, 80000]]

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

print("-------------Distances before Scaling-----------------")

Before_scaling = euclidean_distances([Data[0]],[Data[1]])
print("Distance before scaling : ", Before_scaling[0][0]) # [0][0] -- means first row first column

print("------------------Scaling-----------------")
Scalar = StandardScaler()
Scaled_data = Scalar.fit_transform(Data)

print("----------------Distances after Scaling-----------------")

After_scaling = euclidean_distances([Scaled_data[0]],[Scaled_data[1]])
print("Distance after scaling : ", After_scaling[0][0])

print("\nExplanation:")
print("Before scaling, salary values are much larger than age, so distance is dominated by salary.")
print("After scaling, both features are converted to the same scale, so distance becomes balanced.")
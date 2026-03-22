"""Write a Python program using StandardScaler to perform feature scaling on the following dataset:
[[25, 20000],
[30, 40000],
[35, 80000]]
Print the scaled dataset."""

from sklearn.preprocessing import StandardScaler

Data =[[25, 20000],
[30, 40000],
[35, 80000]]

Scalar = StandardScaler() # Object created
Scaled_data = Scalar.fit_transform(Data) # Apply feature scaling

print("Scaled_data is : \n ", Scaled_data)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

Border = "-"*70

print(Border)
print("Step1 : Load the data")
print(Border)

DataPath = "WinePredictor.csv"
df = pd.read_csv(DataPath)

print(df.head())
print(df.tail())

print(Border)
print("Step2 : Clean, Prepare and Manipulate data")
print(Border)

print("Check missing values : ")
print(df.isnull().sum()) # All values getting 0 -- means no missing values here

"""
axis = 0  → rows
axis = 1  → columns
"""
print (Border)
print("Remove Class column from independent features as 'Class' is dependent feature")

X = df.drop('Class',axis=1)  # axis tells pandas where you want the operation to happen.-- here want to perform operation on column hence Axis - 1
y = df["Class"]

print("X shape : ", X.shape)
print("y shape : ", y.shape)

print(Border)
print("Step3 : Split the data for Training and Testing")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

print("Shape of X_train : ", X_train.shape)
print("Shape of X_test : ", X_test.shape)
print("Shape of y_train : ", y_train.shape)
print("Shape of y_test : ", y_test.shape)

print(Border)
print("Step4 : Create the Model and Train")
print(Border)

model = KNeighborsClassifier() # create the model
model.fit(X_train,y_train)

print("Model trained successfully")

print(Border)
print("Step5 : Test the model")
print(Border)

y_pred = model.predict(X_test)

print(Border)
print("Step6 : Display Actual and Predicted values")
print(Border)

Result = pd.DataFrame({  
    "Actual Values (Class) : ": y_test,
    "Predicted Values (Class) : " : y_pred
})

print(Result)

print(Border)
print("Step7 : Calculate Accuracy")
print(Border)

Accuracy = accuracy_score(y_test,y_pred)
print("Accuracy is : ", round(Accuracy*100),"%")


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

Border = "-" * 70

print(Border)
print("Step1 : Load the data")
print(Border)

DataPath = "Advertising.csv"
df = pd.read_csv(DataPath) # df --> variable name s

print("Data loaded successfully")
print(df.head())
print(df.tail())

print(Border)
print("Step2 : Clean, Prepare and Manipulate data")
print(Border)

if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'], inplace=True)

print("Data after cleaning : ")
print(df.head())
print(df.tail())

print(Border)
print("Step3 : Split dataset into dependent and independent variable")
print(Border)

X = df[["TV","radio","newspaper"]]
y = df["sales"]

print("Shape of X is : ", X.shape)
print("Shape of y is : ", y.shape)

print(Border)
print("Step4 : Split the data for Training and Testing")
print(Border)

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.5,random_state=42)

print("X_train shape : ", X_train.shape)
print("X_test shape : ", X_test.shape)
print("y_train shape : ", y_train.shape)
print("y_test shape : ", y_test.shape)

print(Border)
print("Step5 : Create and Train the model")
print(Border)

model = LinearRegression() # Model created
model.fit(X_train,y_train) # Trained Model

print("Model trained successfully")

print(Border)
print("Step6 : Test the model")
print(Border)

y_pred = model.predict(X_test)

print(Border)
print("Step8 : Display Actual and Predicted values")
print(Border)

# why took DataFrame --> new DataFrame is not the dataset, it is only a result table.
Result = pd.DataFrame({  
    "Actual Values (Sales) : ": y_test.values,
    "Predicted Values (Sales) : " : y_pred
})

# Using pd.set_option('display.max_rows', None) will show all rows.
pd.set_option('display.max_rows', None)

print(Result)

print(Border)
print("Step9 : Plot the graph")
print(Border)

plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual Sales vs Predicted Sales (Linear Regression)")

plt.show()
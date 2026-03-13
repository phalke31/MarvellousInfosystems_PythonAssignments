import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import(accuracy_score,confusion_matrix, ConfusionMatrixDisplay)

border = "-"*50
print("1: Load the data")
print(border)

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)
print("Dataset gets loaded successfully....")
print(df.head())
print(df.tail())

print(border)
print("2: Data Analysis")
print(border)

print("Shape of dataset : ", df.shape)
print("Describe : ", df.describe())
print(df["FinalResult"].value_counts())

print(border)
print("3: Select Features and Target")
print(border)

# Independent variables
X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted","SleepHours"]] # [[ ]] → selects MULTIPLE columns (DataFrame)

# Dependent variables
y = df["FinalResult"] # [ ] → selects ONE column (Series)

print("X shape : ", X.shape)
print("y shape : ", y.shape)

print(border)
print("5: Split dataset into Training and Testing")
print(border)

X_train,X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

""" We have given data 80% : Training and 20% : Testing
80% of 30 = 24 → training
20% of 30 = 6  → testing """

print("X_train shape : ", X_train.shape)
print("X_test shape  : ", X_test.shape)
print("y_train shape : ", y_train.shape)
print("y_test shape : ", y_test.shape)

print(border)
print("6: Train the model")
print(border)

model = DecisionTreeClassifier() # create model
model.fit(X_train, y_train)
print("Model training completed")

print(border)
print("7: Predict test data")
print(border)

y_pred = model.predict(X_test)

print("Actual vs Predicted values")
print(pd.DataFrame({
    "Actual":y_test ,
    "Predicted":y_pred}))

print(border)
print("8: Calculate Model Accuracy")
print(border)

accuracy = accuracy_score(y_test,y_pred)
print("Accuracy of model1 : ", round(accuracy*100),"%")

print(border)
print("9: Confusion Matrix")
print(border)

cm = confusion_matrix(y_test, y_pred)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail","Pass"]
)

display.plot()
plt.show()

# Question 1 :
print("Que1 : use:model.feature_importances_")

"""
Using model.feature_importances_, we can measure how much each feature contributes to prediction.
 The feature with the highest score contributes the most, while the feature with the lowest score contributes the least.
"""
print(border)
print("10: Feature Importance")
print(border)

print("Feature important scores : ")
importances = model.feature_importances_

print("StudyHours : ", importances[0])
print("Attendance :", importances[1])
print("PreviousScore :", importances[2])
print("AssignmentsCompleted :", importances[3])
print("SleepHours :", importances[4])

# Find most important feature 
print("Most important feature : ", X.columns[importances.argmax()])
#  Find least important feature 
print("Least important feature : ", X.columns[importances.argmin()]) #argmin() returns the index of the FIRST smallest value, as in this case we got 4 features as : 0.0 bt it will take 1st one as per columns name

# Question 2 :
print("Que2 : Remove the column SleepHours from the dataset and train model again")

print(border)
print("11: Remove SleepHours and FinalResult")
print(border)

# We are collcting data here (fetures) without SleepHours

X2 = df.drop(columns=["SleepHours", "FinalResult"])
print("Coumns except (SleepHours & FinalResult) : ")
print(X2)

X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y, test_size=0.2, random_state=42)

print("X_train2 shape : ", X_train2.shape)
print("X_test2 shape  : ", X_test2.shape)
print("y_train2 shape : ", y_train2.shape)
print("y_test2 shape : ", y_test2.shape)

print(border)
print("12: Train model without SleepHours")
print(border)

model2 = DecisionTreeClassifier()
model2.fit(X_train2, y_train2)

print("Model Training Completed")

print(border)
print("13: Predict the Test data")
print(border)

y_pred2 = model2.predict(X_test2)

print("Actual v/s Predicted data : ")
print(pd.DataFrame({
      "Actual data":y_test2,
      "Prdicted data":y_pred2})
      )

print(border)
print("14: Calculate model2 Accuracy ")
print(border)

accuracy2 = accuracy_score(y_test2, y_pred2)
print("Model2 accuracy  : ", round(accuracy2*100),"%")

# Compare both model1 and model2 Accuracy :

print(border)
print("15: Compare both model1 and model2 Accuracy")
print(border)

print("Accuracy of model1 : ", round(accuracy*100),"%")
print("Accuracy of model2 : ", round(accuracy2*100),"%")

"""
Does removing SleepHours feature affect performance?
This indicates that SleepHours is not an important feature for predicting FinalResult in this dataset.
"""

# Question 3 :
print("Que3 : Train the model using only : StudyHours / Attendance")

print(border)
print("16: Finding shape of Model : StudyHours / Attendance")
print(border)

X3 = df[["StudyHours","Attendance"]]
y = df["FinalResult"]

print("shape of X3 : ", X3.shape)
print("shape of y : ", y.shape)

print(border)
print("17: Splitting of data")
print(border)

X_train3 , X_test3 , y_train3, y_test3 = train_test_split(X3, y, test_size=0.2, random_state=42)

print("X_train3 shape : ", X_train3.shape)
print("X_test3 shape  : ", X_test3.shape)
print("y_train3 shape : ", y_train3.shape)
print("y_test3 shape : ", y_test3.shape)

print(border)
print("18: Train the Model")
print(border)

model3 = DecisionTreeClassifier()
model3.fit(X_train3, y_train3)

print("Training of Model3 completed")

print(border)
print("19: Predict the test data of features")
print(border)

y_pred3 = model3.predict(X_test3)

print("Actual vs Predicted : ")
print(pd.DataFrame({
    "Actual data": y_test3,
    "Predicted data": y_pred3
}))

print(border)
print("20: Calculate Accuracy")
print(border)

accuracy3 = accuracy_score(y_test3, y_pred3)
print("Accuracy of model3 using only features StudyHours and Attendance: ", round(accuracy3*100),"%")

print(border)
print("21: Compare the accuracy with the full-feature model.")
print(border)

print("Accuracy of model1 means with all features of dataset : ", round(accuracy*100),"%")
print("Accuracy of model3 means with only features StudyHours and Attendance: ", round(accuracy3*100),"%")

# Is the model still performing well? -- Yes

# Question 4 :
print("Que4 : Train the model using only : StudyHours / Attendance")

print(border)
print("22: Create a new DataFrame with details of 5 new students")
print(border)

new_students = pd.DataFrame({
    "StudyHours" : [3,5,2,6,4],
    "Attendance" : [70,85,60,90,75],
    "PreviousScore" : [65,80,55,88,72],
    "AssignmentsCompleted" : [6,9,4,10,7],
    "SleepHours" : [6,7,5,8,6]
})

predictions = model.predict(new_students)

new_students ["Prediction"] = predictions # stored predictions in prediction column which is created due to pandas 
print("New_student values : ")
print(new_students)

# Question 5 : 
print("Que5 : Without using accuracy_score, manually calculate accuracy:")

print(border)
print("23: Without using accuracy_score, manually calculate accuracy:")
print(border)

"""
Manual Accuracy = Total number of predictions(y_pred) / Number of correct prediction len(y_test)"""

correct = 0

for i in range(len(y_test)):
    y_test.iloc[i] == y_pred[i]
    correct += 1

"""Here, y_test[0] will NOT work, because there is no index 0.
We need y_test.iloc[0] → first row by position."""

Manual_Accuracy = correct / len(y_test)

print("Manual Accuracy : ", round(Manual_Accuracy*100),"%")

# Sk learn accuracy
print("By using SL learn Accuracy : ", round(accuracy*100))

# Verify whether it matches sklearn accuracy -- Yes both accuracies are same 

# Question 6 : 
print("Que6 : Identify students where: y_test != y_pred")

print(border)
print("24: Identify students where: y_test != y_pred")
print(border)

wrong = X_test[y_test != y_pred]

print(wrong)
print("Total count of wrong : ", len(wrong))

# Question 7 : 
print("Que7 : Train model using random_state = 0 / 10 / 42")

print(border)
print("25: Train model using random_state = 0 / 10 / 42")
print(border)

for r in [0, 10, 42]:

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state= r
    )

    model = DecisionTreeClassifier() # create model
    model.fit(X_train, y_train) # train the model

    y_pred_temp = model.predict(X_test)

    acc = accuracy_score(y_pred_temp , y_test)
    print("Random state:",r,  "Accuracy is : ", round(acc*100),"%")

# Question 8 : 
print("Que8 : Decision Tree Visualization")

print(border)
print("26: Decision Tree Visualization")
print(border)

# plt.figure(figsize=(12,6))

# plot_tree(
#     model,
#     feature_names=X.columns,
#     class_names=["Fail","Pass"],
#     filled=True
# )

# plt.show()

plt.figure(figsize=(12,6))   
plot_tree(model)
plt.show()

# Question 9 : 
print("Que9 : Create a new column: PerformanceIndex = (StudyHours * 2) + Attendance")

print(border)
print("27: Create a new column: PerformanceIndex = (StudyHours * 2) + Attendance")
print(border)

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X_new = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours","PerformanceIndex"]]

X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)
y_pred_new = model.predict(X_test)

accuracy_new = accuracy_score(y_test, y_pred_new)
print("Accuracy is : ", round(accuracy_new*100),"%")


# Question 10 : 
print("Que10 : Training Accuracy (Overfitting Check)")

print(border)
print("28: Train model with : max_depth = None")
print(border)

model_overfit = DecisionTreeClassifier(max_depth=None)

model_overfit.fit(X_train, y_train)

# Predict on training data
train_pred = model_overfit.predict(X_train)

train_accuracy = accuracy_score(y_train, train_pred)

print("Training Accuracy:", round(train_accuracy*100),"%")



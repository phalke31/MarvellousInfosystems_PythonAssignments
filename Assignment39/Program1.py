
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
print("3: Decide features (X) and label (y)")
print(border)

# Independent variables / Features
X = df[["StudyHours", "Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
# dependent variable / labels
y = df["FinalResult"]

print("X shape : ", X.shape)
print("y Shape : ", y.shape)

print(border)
print("4: Split data into training and testing ")
print(border)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_training data shape : ", X_train.shape)
print("X_testing data shape : ",X_test.shape)

# Questions started here from creating model and other operations :

# Q1 : Create a model object and train it using fit().  
print(border)
print("5: Create a model object and train it using fit()")
print(border)

model = DecisionTreeClassifier() # create model
model.fit(X_train,y_train) # train the model

# Q2 : Use the trained model to predict results for X_test. Display predicted values along with actual values. 
print(border)
print("6: Predict test data ")
print(border)

y_pred = model.predict(X_test)
print("Actual v/s Predicted") 
print(pd.DataFrame({"Actual":y_test, "Predicted":y_pred})) # DataFrame() → pandas class used to create a table
                            # if we use pd.df then it will take original dataset 
            
# Q3 : Calculate model accuracy using accuracy_score. Display the result in percentage format. 
print(border)
print("7: Check Accuracy of model")
print(border)

Accuracy = accuracy_score(y_test,y_pred)
print("Accuracy without percentage : " ,Accuracy) # checks the normal accuracy 
print("Testing Acccuracy :", round(Accuracy*100,2) , "%") # it will covert accuracy into percent 

# Q4. Generate confusion matrix using sklearn. Display it using ConfusionMatrixDisplay. 

print(border)
print("8: Confusion Matrix") # Confusion Matrix is a table that shows how many predictions are correct and how many are wrong.
print(border)

ConfusionMatrix = confusion_matrix(y_test,y_pred) # y_test -- actual , y_pred -- predicted data of labels
display = ConfusionMatrixDisplay(confusion_matrix=ConfusionMatrix, display_labels=[0,1])
display.plot()
plt.show()

"""
Confusion Matrix Explanation:
TP = Predicted Pass & Actually Pass
TN = Predicted Fail & Actually Fail
FP = Predicted Pass & Actually Fail
FN = Predicted Fail & Actually Pass
           Predicted
            0      1
Actual 0   [5]    [0]
Actual 1   [0]    [1] """


#  Q5 : Calculate:  
""" Training accuracy  
 Testing accuracy  

Compare both and comment whether the model is overfitting or underfitting.""" 

print(border)
print("9: Taining v/s Testing Accuracy ") 
print(border)

# Training prediction : why y_train not passed -- prediction means we don’t know the answer yet hence only X-train passed
y_train_pred = model.predict(X_train)

# Training accuracy
training_accuracy = accuracy_score(y_train, y_train_pred)
print("Training Accuracy : ",round(training_accuracy*100,2), "%")

# Testing Accuracy 
testing_accuracy = accuracy_score(y_test, y_pred)
print("Testing Accuracy : ", round(testing_accuracy*100,2),"%")

# Overfitting / Underfitting check

print("Model Observation:")

if training_accuracy > testing_accuracy:
    print("Model may be Overfitting (training accuracy higher than testing)")
elif training_accuracy < testing_accuracy:
    print("Model may be Underfitting")
else:
    print("Model performance is balanced")

# Q6 : Train three Decision Tree models with: 
"""
- max_depth = 1  
- max_depth = 3  
- max_depth = None  

Compare their testing accuracies and write your observations.""" 

print(border)
print("10: Train below 3 Decision Tree Models") 
print(border)

# max_depth = 3  
model_depth3 = DecisionTreeClassifier(max_depth=3)
model_depth3.fit(X_train,y_train)

pred3 = model_depth3.predict(X_test)
accuracy3 = accuracy_score(y_test,pred3)

print("Testing Accuracy of max_depth = 3 :", round(accuracy3*100,2), "%")

# max_depth = 1

model_depth1 = DecisionTreeClassifier(max_depth=1)
model_depth1.fit(X_train,y_train)

pred1 = model_depth1.predict(X_test)
accuracy1 = accuracy_score(y_test, pred1)

print("Testing accuracy of max_depth = 1 : ", round(accuracy1*100,2),"%")

# max_depth = None

model_depth_None = DecisionTreeClassifier(max_depth=None)
model_depth_None.fit(X_train, y_train)

pred_None = model_depth_None.predict(X_test)
accuracy_none = accuracy_score(y_test, pred_None)

print("Testing acuracy of max_depth = None : ", round(accuracy_none*100,2),"%")


# Q7. Use the trained model to predict result for a student with:  
""" StudyHours = 6  
- Attendance = 85  
- PreviousScore = 66  
- AssignmentsCompleted = 7 """

print(border)
print("11: Use the trained model to predict result for a student") 
print(border)

new_student = pd.DataFrame(
    [[6,85,66,7,7]],
    columns=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
)
prediction = model.predict(new_student)

print("Predicted value :", prediction)

if prediction[0] == 1:
    print("The student will PASS")
else:
    print("The student will FAIL")


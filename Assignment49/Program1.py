
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, confusion_matrix, recall_score
from sklearn.preprocessing import StandardScaler

# 1. Exploratory Data Analysis (EDA):
Border = "-"*70

print(Border)
print("Step 1 : Load the dataset")
print(Border)

df = pd.read_csv("diabetes.csv")
print(df.head())
print(df.tail())

print(Border)
print("Step 2 : Basic Information")
print(Border)

print("Dataset Information")
print(df.describe())

print("Check null values")
print(df.isnull().sum())

print("Summary")
print(df.describe())

print("Original shape")
print(df.shape)

print(Border)
print("Step3 : Plot the distribution of the target variable (Outcome)")
print(Border)

df['Outcome'].value_counts().plot(kind='bar')

plt.title("Distribution of Diabetes Outcome")
plt.xlabel("Outcome (0 = No Diabetes, 1 = Diabetes)")
plt.ylabel("Count")
plt.show()

# 2. Data Preprocessing:

print(Border)
print("Step4 : Data Preprocessing")
print(Border)

# Replace zero values with NaN
col = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
df[col] = df[col].replace(0, np.nan) # np.nan - not a number --> replace 0 with nan in column

# Fill missing values with median
df.fillna(df.median(), inplace=True)

print("Missing values handled successfully")

# Separate input and output

X = df.drop('Outcome',axis=1)  # axis=1 : column , axis=0 : row
y = df['Outcome']

print("Shape of X : ", X.shape)
print("Shape of y : ", y.shape)

print(Border)
print("Step5 : Apply feature scaling using StandardScaler or MinMaxScaler")
print(Border)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) # here on X columns we have applied this feature to get value in same range 

print(Border)
print("Step6 : Split the dataset into Training and Testing")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(X_scaled,y,test_size=0.2,random_state=42)

print("Shape of X_train : ", X_train.shape)
print("Shape of X_test : ", X_test.shape)
print("Shape of y_train : ", y_train.shape)
print("Shape of y_test : ", y_test.shape)

# 3. Model Building:

print(Border)
print("Step7 : Find the best value of K using KNN")
print(Border)

accuracy_scores = []

for k in range(1,21):
    model = KNeighborsClassifier(n_neighbors=k) # n_neighbors = k means how many nearest data points the model should use to make a prediction.

    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_pred,y_test)
    print("K = ", k, "Accuracy is : ", acc)
    accuracy_scores.append(acc)

# Automatic way to find best value of k

best_k = accuracy_scores.index(max(accuracy_scores))+1
print("Best vaues of k is : ", best_k)

print(Border)
print("Step8 : Build Final Model")
print(Border)

final_model = KNeighborsClassifier(n_neighbors=best_k) # Final model created
final_model.fit(X_train, y_train) # model trained

print("Final KNN Model trained successfully")

y_pred = final_model.predict(X_test)

Result = pd.DataFrame({
    "Actual test result" : y_test,
    "Prediction Result" : y_pred
})
print(Result)

print(Border)
print("Step9 : Model Evaluation - Accuracy")
print(Border)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of KNN Model is : ", round(accuracy*100,2),"%") # Accuracy = (TP + TN) / Total = (81 + 33) / 154 = 74%

print(Border)
print("Step10 : Confuion Matrix")
print(Border)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix of KNN model is : ")
print(cm)

print(Border)
print("Step11 : Precision, Recall and F1 Score")
print(Border)

print("Precision : ", precision_score(y_test,y_pred)) # When the model says “this patient has diabetes”, it is correct 65% of the time --> So some patients predicted as diabetic were actually healthy.
print("Recall : ", recall_score(y_test, y_pred)) # Out of all real diabetes patients, the model was able to detect only 60% --> That means the model is missing some diabetic patients.
print("F1 : ", f1_score(y_test, y_pred)) # Overall balance between precision and recall is 62% --> model performance is moderate, not very strong but not bad for a beginner model.

print(Border)
print("Step12 : Plot the graph to visualize confusion matrix for KNN")
print(Border)

plt.imshow(cm)
plt.title("Confusion Matrix for KNN")
plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")

plt.colorbar()
plt.show()

print(Border)
print("Step13 : Logistic Regression Model")
print(Border)

Log_Model = LogisticRegression(max_iter=1000) # Logistic Regression model created
Log_Model.fit(X_train, y_train) # Model trained
ypred_LogModel = Log_Model.predict(X_test)

Result1 = pd.DataFrame({
    "Actual test result" : y_test,
    "Prediction Result" : ypred_LogModel
})
print(Result1)

accuracy_Log_Model = accuracy_score(y_test, ypred_LogModel)
print("Accuracy of Logistic Regression is : ", round(accuracy_Log_Model*100,2),"%")

cm_Log_Model = confusion_matrix(y_test, ypred_LogModel)
print("Confusion matrix of Logistic Regression Model is : ")
print(cm_Log_Model)

print("Precison : ",precision_score(y_test, ypred_LogModel))
print("Recall : ", recall_score(y_test,ypred_LogModel))
print("F1 : ", f1_score(y_test, ypred_LogModel))

# Plot the graph for confusion matrix of Logistic Regression Model
plt.imshow(cm_Log_Model)
plt.title("Confusion Matrix of Logistic Regression Model")
plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")

plt.colorbar()
plt.show()

print(Border)
print("Step14 : Decison Tree Model")
print(Border)

Tree_Model = DecisionTreeClassifier(random_state=42) # Decsion Tree model created
Tree_Model.fit(X_train,y_train) # Model trained

ypred_TreeModel = Tree_Model.predict(X_test)

Result2 = pd.DataFrame({
    "Actual test result" : y_test,
    "Prediction Result" : ypred_TreeModel
})
print(Result2)

accuracy_TreeModel = accuracy_score(y_test, ypred_TreeModel)
print("Accuracy of Decision Tree Model is : ", round(accuracy_TreeModel*100,2),"%")

print("Precison : ", precision_score(y_test,ypred_TreeModel))
print("Recall : ", recall_score(y_test,ypred_TreeModel))
print("F1 : ", f1_score(y_test, ypred_TreeModel))

cm_TreeModel = confusion_matrix(y_test, ypred_TreeModel)
print("Confusion Matrix of Decision Tree Classifier is : ")
print(cm_TreeModel)

# Plot the graph of Confusion Matrix of Decision Tree Classifier

plt.imshow(cm_TreeModel)

plt.title("Confusion Matrix of Decision Tree Classifier")
plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")

plt.colorbar()
plt.show()

print(Border)
print("Step15 : Accuracy of all Models : KNN , Decison Tree, Logistic Regression")
print(Border)

print("Accuracy of KNN Model is : ", round(accuracy*100,2),"%")
print("Accuracy of Log_Model is : ", round(accuracy_Log_Model*100,2),"%")
print("Accuracy of Decision Tree Model is : ", round(accuracy_TreeModel*100,2),"%")

print(Border)
print("Step16 : Accuracy of all Models : KNN , Decison Tree, Logistic Regression")
print(Border)

print("Accuracy of KNN Model is : ", round(accuracy*100,2),"%")
print("Accuracy of Log_Model is : ", round(accuracy_Log_Model*100,2),"%")
print("Accuracy of Decision Tree Model is : ", round(accuracy_TreeModel*100,2),"%")

print(Border)
print("Step16 : Save predicted changes of KNN Model in New CSV file")
print(Border)

Result.to_csv("diabetes_predictions_KNN.csv", index=False)
Result1.to_csv("diabetes_predictions_Log.csv", index=False)
Result2.to_csv("diabetes_predictions_Tree.csv", index=False)

print("Actual and Predicted Results has been saved successfully in CSV files")














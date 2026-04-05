
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

# 1. Exploratory Data Analysis (EDA):
Border = "-"*70

print(Border)
print("Step1 : Load the dataset")
print(Border)

df = pd.read_csv("bank-full.csv", sep=";")
print(df.head())
print(df.shape)

print(Border)
print("Step2 : Basic Information")
print(Border)

print("Summary : \n", df.describe()) 
print("\nInformation : \n ")
df.info()
print(df['y'].value_counts())

df['y'].value_counts().plot(kind="bar")
plt.title("Class distribution(Yes/No)")
plt.show()

print(Border)
print("Step3 : Handle Missing / Unknown values")
print(Border)

# replace unknown values with nan
df.replace('unknown', np.nan, inplace=True)

# fill missing values
df = df.ffill() #Fill missing values using previous row value

print("Missing values handled successfully")

print(Border)
print("Step4 : Encoding Categorical data")
print(Border)

# convert target variable into numeric
df['y'] = df['y'].map({'yes':1, 'no':0})

# label encoding for categorical columns
categorical_cols = df.select_dtypes(include=['object', 'string']).columns

for col in categorical_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

print("Encoding completed")

print(Border)
print("Step5 : Feature Scaling")
print(Border)

X = df.drop('y',axis=1)
y = df['y']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Scaling done")

print(Border)
print("Step6 : Train Test split the model")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(X_scaled,y,test_size=0.2,random_state=42)

print("X_train shape :",X_train.shape)
print("X_test shape :",X_test.shape)
print("y_train shape :",y_train.shape)
print("X_test shape :",y_test.shape)

print(Border)
print("Step7 : Train the models")
print(Border)

# Logistic Regression
LR = LogisticRegression()
LR.fit(X_train,y_train)

# KNN
KNN = KNeighborsClassifier(n_neighbors=5)
KNN.fit(X_train,y_train)

# Random forest classifier
RFC = RandomForestClassifier()
RFC.fit(X_train,y_train)

print("Model trained successfully")

print(Border)
print("Step8 : Model Evaluation")
print(Border)

# Logistic Regression
print("Logistic Regression")

y_pred_LR = LR.predict(X_test)
print("Predictions : ", y_pred_LR)

print("Accuracy of LR model is : ", accuracy_score(y_test,y_pred_LR))
print("Confusion Matrix : ", confusion_matrix(y_test,y_pred_LR))
print("Classification Report : \n", classification_report(y_test,y_pred_LR))

roc_LR = roc_auc_score(y_test, LR.predict_proba(X_test)[:,1])
print("ROC-AUC Score:", roc_LR)

# KNN 
print("K-Nearest Neighbours")

y_pred_KNN = KNN.predict(X_test)
print("Predictions : ", y_pred_KNN)

print("Accuracy of KNN model is : ", accuracy_score(y_test,y_pred_KNN))
print("Confusion Matrix : ", confusion_matrix(y_test,y_pred_KNN))
print("Classification Report : \n", classification_report(y_test,y_pred_KNN))

roc_KNN = roc_auc_score(y_test, KNN.predict_proba(X_test)[:,1])
print("ROC-AUC Score:", roc_KNN)

print("Random Forest classifier")
y_pred_RFC = RFC.predict(X_test)
print("Predictions : ", y_pred_RFC)

print("Accuracy of RFC model is : ", accuracy_score(y_test,y_pred_RFC))
print("Confusion Matrix : ", confusion_matrix(y_test,y_pred_RFC))
print("Classification Report : \n", classification_report(y_test,y_pred_RFC))

roc_RFC = roc_auc_score(y_test, RFC.predict_proba(X_test)[:,1])
print("ROC-AUC Score:", roc_RFC)

print(Border)
print("Step9 : ROC Curve")
print(Border)

from sklearn.metrics import roc_curve

plt.figure()

# Logistic Regression
y_prob_lr = LR.predict_proba(X_test)[:,1]
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
plt.plot(fpr_lr, tpr_lr, label="Logistic Regression")

# KNN 
y_prob_knn = KNN.predict_proba(X_test)[:,1]
fpr_knn, tpr_knn, _ = roc_curve(y_test, y_prob_knn)
plt.plot(fpr_knn, tpr_knn, label="KNN")

# Random Forest 
y_prob_rf = RFC.predict_proba(X_test)[:,1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
plt.plot(fpr_rf, tpr_rf, label="Random Forest")

# Diagonal line (random model)
plt.plot([0,1], [0,1], 'k--')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.legend()
plt.show()

print(Border)
print("Step10 : Confusion Matrix Visualization")
print(Border)

# Logistic Regression 
cm_lr = confusion_matrix(y_test, y_pred_LR)

plt.figure()
sns.heatmap(cm_lr, annot=True, fmt='d')

plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# KNN

cm_knn = confusion_matrix(y_test, y_pred_KNN)

plt.figure()
sns.heatmap(cm_knn, annot=True, fmt='d')

plt.title("KNN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# Random Forest classifier

cm_rf = confusion_matrix(y_test, y_pred_RFC)

plt.figure()
sns.heatmap(cm_rf, annot=True, fmt='d')

plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
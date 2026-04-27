
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

Border = "-"*70

print(Border)
print("Step1 : Load the dataset")
print(Border)

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

print("Data loaded successfully")

print("fake data shape : ", fake.shape)
print("true data shape : ", true.shape)

print(Border)
print("Step2 : Add label column")
print(Border)

fake['label'] = 0
true['label'] = 1

print("Labels added successfully")

print(Border)
print("Step3 : Combine the datasets")
print(Border)

df = pd.concat([fake,true], axis=0) # axis == 0 --> it will add the data row wise 
print("Combined shape : ", df.shape)

print(Border)
print("Step4 : Select useful columns")
print(Border)

# Combine title + text
df['content'] = df['title'] + " " + df['text']

# Keep only required columns
df = df[['content', 'label']]

print(df.head())

print(Border)
print("Step5 : Handle missing values")
print(Border)

df.dropna(inplace=True)
print("Missing values removed")

print(Border)
print("Step6 : Define X and y")
print(Border)

X = df['content']
y = df['label']

print(Border)
print("Step7 : Use TF-IDF Vectorization to convert text into numerical features")
print(Border)
                                                       # max_df=0.7 --> Removes words appearing in >70% documents
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7) # stop_words='english' --> avoid duplicate word like is, the, and 

X_tfidf = tfidf.fit_transform(X) # Conversion process will takes place

print("Converted data from text to numbers successfully")

print(Border)
print("Step8 : Train Test Split the model")
print(Border)

X_train , X_test , y_train, y_test = train_test_split(X_tfidf,y,test_size=0.2,random_state=42)

print("X_train shape :", X_train.shape)
print("X_test shape :", X_test.shape)

print(Border)
print("Step9 : Train Models")
print(Border)

# Logistic Regression

lr = LogisticRegression()
lr.fit(X_train,y_train)

# Decision Tree Classifier
dt = DecisionTreeClassifier()
dt.fit(X_train,y_train)

print("Models trained successfully")

print(Border)
print("Step10 : Voting Classifier")
print(Border)

# Hard voting : Counts model predictions and picks the majority. (It's good if odd models are there)

hard_vote = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)], # Estimators = collection of models that VotingClassifier will combine
    voting='hard'
)
hard_vote.fit(X_train,y_train)

# Soft voting : Averages model probabilities and picks the highest.

soft_vote = VotingClassifier(
    estimators=[('lr',lr),('dt',dt)],
    voting='soft'
)
soft_vote.fit(X_train, y_train)

print("Voting models created successfully")

print(Border)
print("Step11 : Model Evaluation")
print(Border)

# Logistic Regression
y_pred_lr = lr.predict(X_test)
print("Accuracy of Logistic Regression :", accuracy_score(y_test,y_pred_lr))
print("Confusion Matrix : \n ", confusion_matrix(y_test,y_pred_lr))

# Decision Tree
y_pred_dt = dt.predict(X_test)
print("Accuracy of Decision Tree :", accuracy_score(y_test,y_pred_dt))
print("Confusion Matrix : \n ", confusion_matrix(y_test,y_pred_dt))

# Hard voting
y_pred_hard = hard_vote.predict(X_test)
print("Accuracy of hard vote :", accuracy_score(y_test,y_pred_hard))
print("Confusion Matrix : \n " , confusion_matrix(y_test,y_pred_hard))

# Soft voting
y_pred_soft = soft_vote.predict(X_test)
print("Accuracy of soft vote :", accuracy_score(y_test,y_pred_soft))
print("Confusion Matrix : \n ", confusion_matrix(y_test,y_pred_soft))

print(Border)
print("Step12 : Classification Report of Models")
print(Border)

print("\nLogistic Regression Report:\n")
print(classification_report(y_test, y_pred_lr))

print("\nDecision Tree Report:\n")
print(classification_report(y_test, y_pred_dt))

print("\nHard Voting Report:\n")
print(classification_report(y_test, y_pred_hard))

print("\nSoft Voting Report:\n")
print(classification_report(y_test, y_pred_soft))












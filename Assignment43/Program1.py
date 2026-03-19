import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


border = "-"*50
print("Step1: Load the data")
print(border)

DatasetPath = "PlayPredictor.csv"
df = pd.read_csv(DatasetPath)
print("Dataset gets loaded successfully....")
print("\n",df.head())
print("\n",df.tail())

print(border)
print("Step2: Clean, Prepare, and Manipulate Data")
print(border)

# Create label encoder
le_Whether = LabelEncoder()
le_Temperature = LabelEncoder()
le_Play = LabelEncoder()

# Apply label encoder on all 
df["Whether"] = le_Whether.fit_transform(df["Whether"])
df["Temperature"] = le_Temperature.fit_transform(df["Temperature"])
df["Play"] = le_Play.fit_transform(df["Play"])

print(border)
print("Step3: Train the data (Using KNN)")
print(border)

X = df[["Whether","Temperature"]]
y = df["Play"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
print("Model trained successfully")

print(border)
print("Step4: Test Data")
print(border)

# Take input from user
Whether_input = input("Enter Weather (Sunny / Overcast / Rainy): ").strip().capitalize()
Temperature_input = input("Enter Temperature (Hot / Mild / Cool): ").strip().capitalize()

# Encode input using same encoders
Whether_encoded = le_Whether.transform([Whether_input])[0]
temp_encoded = le_Temperature.transform([Temperature_input])[0]

# Prediction
prediction = model.predict([[Whether_encoded, temp_encoded]])

if prediction[0] == 1:
    print("Prediction: Yes (Play)")
else:
    print("Prediction: No (Don't Play)")

print(border)
print("Step 5 : Calculate Accuracy")
print(border)

def CheckAccuracy():

    X = df[["Whether","Temperature"]]
    y = df["Play"]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.5,random_state=42)

    for k in range(1,8):

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,y_train)

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test,y_pred)

        print("Accuracy for K =",k,"is :",round(acc*100,2),"%")

CheckAccuracy()


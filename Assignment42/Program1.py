
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Que1 : Implement Simple Linear Regression manually without using any ML library.
print ("-------------------------Question1-------------------------------------")

X = [1,2,3,4,5]
Y = [3,4,2,4,5]

Border = "-"*60
print("Step 1 : Mean of X (X̄)")
n = len(X)
mean_X = sum(X) / len(X)
print("Mean of X is : ", mean_X) # Mean = 3.0

print(Border)
print("Step 2 : Mean of Y (Ȳ)")

m = len(Y)
mean_Y = sum(Y) / len(Y)
print("Mean of Y is : ", mean_Y) # Mean = 3.6

print(Border)
print("Step 3 : Find slope")

"""
Formula of slope :
m(slope) = ∑(Xi​−Xˉ)(Yi​−Yˉ)​ / ∑(Xi​−Xˉ) **2 """

numerator = 0
denominator = 0

for i in range(len(X)):

    numerator += (X[i] - mean_X)*(Y[i] - mean_Y)
    denominator += (X[i] - mean_X)**2

m = numerator/denominator
print("Slope of line : ", m)
print("Slope (m) =", round(m,2)) # (m,2) -- 2 is used to calculate values as per mathematics (eg. 0.3999999 --> 0.40)


print(Border)
print("Step 4 : Find Intercept (c)")
# Formula of Intercept : c=Yˉ−(m×Xˉ)

c = mean_Y - (m * mean_X)
print("Intercept(c) is : ", c)

print(Border)
print("Step 5 : Regression of Equation (y=mx+c)")

print("Y = ", round(m,2),"X +", round(c,2))

print(Border)
print("Step 6 : Predicted Y for x_new = 6")

x_new = 6
y_pred = m * x_new + c

print("Predicted Y for X = 6 :", round(y_pred,2))

print ("-------------------------Question2-------------------------------------")

y_pred = []

for x in X :
    y_pred.append(m*x + c)

print(y_pred)

MSE = mean_squared_error(Y, y_pred) 
print("Mean Squared Error : ", MSE)

R2 = r2_score(Y, y_pred)
print("R square value :",R2)

print ("-------------------------Question3-------------------------------------")

experience = [1,2,3,4,5]
salary = [20000,25000,30000,35000,40000]

print(Border)
print("Step 1 : Calculate mean")

mean_x = sum(experience)/len(experience)
mean_y = sum(salary) / len(salary) 

print("Mean of experience : ", mean_x) # 3.0
print("Mean of salary : ", mean_y) # 30000.0

print(Border)
print("Step 2 : Calculate Slope")

# slope = m*x + c

numerator = 0
denominator = 0

for i in range(len(experience)):

    numerator += (experience[i] - mean_x)*(salary[i] - mean_y)
    denominator += (experience[i] - mean_x)**2

m = numerator/denominator
print("Slope of line : ", m)
print("Slope (m) =", round(m,2)) # 5000.0

print(Border)
print("Step 3 : Find intercept(c)")

c = mean_y - (m * mean_x)
print("Intercept(c) is : ", c) # 15000.0

print(Border)
print("Step 4 : Regression of Equation (y=mx+c)")

print("Y =",round(m,2),"X +",round(c,2))

print(Border)
print("Step 5 : Predicted salay for 6 year of experience (X_new = 6)")

X_new = 6
Y_pred = m*X_new + c
print("Y_pred (Prediceted salary) : ", Y_pred)
      
print(Border)
print("Step 6 : Create regression line values (Y_pred) for all X values")

Y_pred = []

for X in experience:
    Y_pred.append(m*X + c)

print("Predicted values of salary (Y_pred) is : ", Y_pred)

print(Border)
print("Step 7 : Plot Graph")

plt.scatter(experience, salary) # Actual data
plt.plot(experience, Y_pred) # Regression line(Predicted data)

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Salary Prediction using Linear Regression")

plt.show()


"""
we can't see scatter points in graph because the predicted values and actual values are exactly the same in dataset
So the scatter points lie exactly on the regression line, and the line covers the dots.
"""
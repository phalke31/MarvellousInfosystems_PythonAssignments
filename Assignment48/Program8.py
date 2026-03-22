"""Write a Python program that calculates TP, TN, FP, FN for the following arrays:

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

Display all four values."""

# 1 → True / Positive  
# 0 → False / Negative

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

TP = 0
TN = 0
FP = 0
FN = 0

for i in range(len(actual)):

    if actual[i] == 1 and predicted[i]== 1:
        TP += 1
    elif actual[i] == 0 and predicted[i] == 0:
        TN += 1
    elif actual[i] == 0 and predicted[i] == 1:
        FP += 1
    elif actual[i] == 1 and predicted[i] == 0:
        FN += 1

print("True Postitive : ", TP)
print("True Negatie : ", TN)
print("False Postitive : ", FP)
print("False Negative : ", FN)
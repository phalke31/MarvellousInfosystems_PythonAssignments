"""3: Write a Python program to implement a class named Arithmetic with the following characteristics:
The class should contain two instance variables: Value1 and Value2.
Define a constructor (__init__) that initializes all instance variables to 0.
Implement the following instance methods:
Accept() - accepts values for Value1 and Value2 from the user.
Addition() - returns the addition of Value1 and Value2.
Subtraction() - returns the subtraction of Value1 and Value2.
Multiplication() - returns the multiplication of Value1 and Value2.
Division() - returns the division of Value1 and Value2 (handle division by zero properly).
Create multiple objects of the Arithmetic class and invoke all the instance methods."""

class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter value1 : "))
        self.value2 = int(input("Enter value2 : "))
    
    def Addition(self):
        return self.value1 + self.value2
    
    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        if self.value2 == 0:
            return "Cannot divide by zero"
        return self.value1 / self.value2
    
# created objects of aritmatic class
A1 = Arithmetic()
A2 = Arithmetic()

# Call methods for first object : A1
A1.Accept()
print("Addition:", A1.Addition())
print("Subtraction:", A1.Subtraction())
print("Multiplication:", A1.Multiplication())
print("Division:", A1.Division())

# Call methods for second object : A2
A2.Accept()
print("Addition:", A2.Addition())
print("Subtraction:", A2.Subtraction())
print("Multiplication:", A2.Multiplication())
print("Division:", A2.Division())
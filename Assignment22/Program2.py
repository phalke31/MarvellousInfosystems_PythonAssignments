"""2: Write a Python program to implement a class named Circle with the following requirements:
The class should contain three instance variables: Radius, Area, and Circumference.
The class should contain one class variable named PI, initialized to 3.14.
Define a constructor (__init__) that initializes all instance variables to 0.0.
Implement the following instance methods:
Accept() - accepts the radius of the circle from the user.
CalculateArea() - calculates the area of the circle and stores it in the Area variable.
CalculateCircumference() - calculates the circumference of the circle and stores it in the Circumference variable.
Display() - displays the values of Radius, Area, and Circumference.
Create multiple objects of the Circle class and invoke all the instance methods for each object."""

class Circle: # class
    PI = 3.14 # class variable

    def __init__(self): # instance method
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # accept radius from user
    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # display all values of circle

    def Display(self):
        print("Radius is : ", self.Radius)
        print("Area is : ", self.Area)
        print("Circumference is : ", self.Circumference)

# created objects :
C1 = Circle()
C2 = Circle()

# Call methods for first object
C1.Accept()
C1.CalculateArea()
C1.CalculateCircumference()
C1.Display()

# Call methods for second object
C2.Accept()
C2.CalculateCircumference()
C2.CalculateArea()
C2.Display()
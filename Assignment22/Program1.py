"""1: Write a Python program to implement a class named Demo with the following specifications:
The class should contain two instance variables: no1 and no2.
The class should contain one class variable named Value.
Define a constructor __init__() that accepts two parameters and initializes the instance variables.
Implement two instance methods:
Fun() - displays the values of instance variables no1 and no2.
Gun() - displays the values of instance variables no1 and no2.
Create two objects of the Demo class as follows:

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)"""

class Demo: # class
    Value = 5 # class variable

    def __init__(self, no1, no2): # constructor
        self.no1 = no1 # instance variable
        self.no2 = no2 # instance variable

    def fun(self): # instance method
        print(self.no1, self.no2) # print instance variables

    def gun(self):
        print(self.no1, self.no2) # print instance variables

# create objects 
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Call methods
Obj1.fun()
Obj1.gun()

Obj2.fun()
Obj2.gun()

# Print class variable
print(Demo.Value)





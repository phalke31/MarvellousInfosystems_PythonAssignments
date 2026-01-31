"""3: Write a Python program to implement a class named Numbers with the following specifications:
The class should contain one instance variable:
Value
Define a constructor (__init__) that accepts a number from the user and initializes Value.
Implement the following instance methods:
ChkPrime() - returns True if the number is prime, otherwise returns False
ChkPerfect() - returns True if the number is perfect, otherwise returns False
Factors() - displays all factors of the number
SumFactors() - returns the sum of all factors
(You may use this method as a helper in ChkPerfect() if required)
Create multiple objects and call all methods."""

class Numbers:
    
    def __init__(self, value):
        self.value = value
    
    def Chkprime(self):
        No = self.value
        if (No <= 1):
            return False # print("Not prime")
        for i in range(2, No):
            if No % i == 0:
                return False # print("Not prime")
        return True # print("It's prime number")
    
    def ChkPerfect(self):
        No = self.value
        total = 0

        for i in range(1,No):
            if (No % i == 0):
                total = total + i
        
        if No == total:
            return True
        else:
            return False
    
    def Factors(self):
        No = self.value

        for i in range(1, No + 1):    
            if (No % i == 0):
                print(i)
    
    def Sum_of_Factors(self):
        No = self.value
        sum = 0

        for i in range(1, No+1):
            if No % i == 0:
                sum = sum + i
        return sum
    
    # Create objects
Num1 = Numbers(6)
Num2 = Numbers(8)

print("------------Num1--------------")
print("Num1 Results: ")
print("Is perfect?", Num1.ChkPerfect())
print("Is prime?", Num1.Chkprime())
print("Factors of Num1 are : ")
Num1.Factors()              
print("Sum of factors:", Num1.Sum_of_Factors())

print("------------Num2--------------")

print("Num2 Results:")
print("Is perfect?", Num2.ChkPerfect())
print("Is prime?", Num2.Chkprime())
print("Factors of Num2 are : ")
Num2.Factors()              
print("Sum of factors:", Num2.Sum_of_Factors())




""" 2. Write a Python program to implement a class named BankAccount with the following requirements:
The class should contain two instance variables:
Name (Account holder name)
Amount (Account balance)
The class should contain one class variable:
ROI (Rate of Interest), initialized to 10.5
Define a constructor (__init__) that accepts Name and initializes other members.
Implement the following instance methods:
Display() - displays account holder name and current balance
Deposit() - accepts an amount from the user and adds it to balance
Withdraw() - accepts an amount from the user and subtracts it from balance
CalculateInterest() - calculates and returns interest using formula:
Interest = (Amount * ROI) / 100
Create multiple objects and demonstrate all methods"""

class BankAccount:
    ROI = 10.5  # Class variable for rate of interest

    def __init__(self, Name):
        self.Name = Name
        self.Amount = 0.0  # Initial balance

    # Display account details
    def Display(self):
        print(self.Name, "Balance:", self.Amount)

    # Deposit amount
    def Deposit(self):
        amt = float(input("Deposit amount: "))
        self.Amount += amt

    # Withdraw amount
    def Withdraw(self):
        amt = float(input("Withdraw amount: "))
        if amt > self.Amount:
            print("Insufficient balance")
        else:
            self.Amount -= amt

    # Calculate interest 
    def CalculateInterest(self):
        return (self.Amount * self.ROI) / 100


# Objects created
Account1 = BankAccount("Shreya")
Account2 = BankAccount("Varun")

# 1st account
Account1.Deposit()
Account1.Withdraw()
Account1.Display()
print("Interest:", Account1.CalculateInterest())

# 2nd account
Account2.Deposit()
Account2.Withdraw()
Account2.Display()
print("Interest:", Account2.CalculateInterest())

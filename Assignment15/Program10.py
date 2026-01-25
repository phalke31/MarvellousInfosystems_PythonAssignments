"""10. Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers."""

Number = [1,2,3,4,5,6,7,8,9,10]

# to print how list of even number
Data_after_filter = list(filter(lambda a : a%2==0, Number))
print(Data_after_filter)

Count = len(Data_after_filter)
print("Count of even number is : ", Count)
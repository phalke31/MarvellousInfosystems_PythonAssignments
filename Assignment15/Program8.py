"""Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5."""

Numbers = [3,5,7,9,12,13,15,20,25,14,17]

Data_after_filter = list(filter(lambda a : a % 3 == 0 and a % 5 == 0, Numbers))
print(Data_after_filter)
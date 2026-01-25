""" Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5."""

String_list = ["Shreya", "Ketaki", "Purva", "Payal", "Anjali"]
print(String_list)

Data_after_filter = list(filter(lambda a : len(a) > 5, String_list))
print(Data_after_filter)

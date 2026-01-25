""" Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5."""

String_list = ["Shreya", "Ketaki", "Purva", "Payal", "Anjali"]
print(String_list)

Length_of_string = list(filter(lambda a : a>5, String_list))
print(Length_of_string)

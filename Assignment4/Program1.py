""" Write a program which accepts one character and checks whether it is vowel or consonant.
Input: a
Output: Vowel """


Character = input("Enter character : ").lower()

if Character in ('a', 'e', 'i', 'o', 'u'):
    print("It's Vowel")
else:
    print("It's Consonant")


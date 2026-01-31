"""5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one 
list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers.
 Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use 
 normal functions instead of lambda functions).  

Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62"""

from functools import reduce

numbers = [2, 70, 11, 10, 17, 23, 31, 77]

def is_prime(Num):
    if Num <= 1:
        return False
    for i in range(2, Num):
        if Num % i == 0:
            return False
    return True

# filter
prime_numbers = list(filter(is_prime, numbers))
print("List after filter:", prime_numbers)

# map
double_of_prime_numbers = list(map(lambda x: x * 2, prime_numbers))
print("List after map:", double_of_prime_numbers)

# reduce
maximum = reduce(lambda a, b: a if a > b else b, double_of_prime_numbers)
print("Output of reduce:", maximum)
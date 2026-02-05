"""1: Design a Python application that creates two threads named Prime and NonPrime.
Both threads should accept a list of integers.
The Prime thread should display all prime numbers from the list.
The NonPrime thread should display all non-prime numbers from the list."""

import threading

Numbers = list(map(int, input("Enter numbers : ").split()))
lock = threading.Lock()

def is_prime(Numbers):
    if Numbers <= 1:
        return False # 0 and 1 are not prime 
    for i in range(2, Numbers):
        if Numbers % i == 0:
            return False
    return True

lock.acquire()
def Prime(Numbers):
    print("Prime numbers in list are : ")
    for num in Numbers:
        if is_prime(num):
            print(num, end=" ")
    print()
    lock.release()

def Non_prime(Numbers):
    lock.acquire()
    print("Non prime numbers in list are : ")
    for num in Numbers:
        if not is_prime(num):
            print(num, end= " ")
    print()
    lock.release()

Prime_thread = threading.Thread(target=Prime, args=(Numbers, ))
Non_prime_thread = threading.Thread(target=Non_prime, args=(Numbers, ))

Prime_thread.start()
Non_prime_thread.start()

Prime_thread.join()
Non_prime_thread.join()


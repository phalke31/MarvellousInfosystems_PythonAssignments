"""2. Design a Python application that creates two threads named EvenFactor and OddFactor:
Both threads should accept one integer number as a parameter.

The EvenFactor thread should:
○ Identify all even factors of the given number.
○ Calculate and display the sum of even factors.

The OddFactor thread should:
○ Identify all odd factors of the given number.
○ Calculate and display the sum of odd factors.

After both threads complete execution, the main thread should display the message:
“Exit from main”
"""

import threading

number = int(input("Enter a number: "))

# Function to find even factors
def even_factors(num):
    total = 0
    print("Even factors of", num, ":")
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:   # factor AND even
            print(i)
            total += i
    print("Sum of even factors:", total)

# Function to find odd factors
def odd_factors(num):
    total = 0
    print("Odd factors of", num, ":")
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:   # factor AND odd
            print(i)
            total += i
    print("Sum of odd factors:", total)

# Create threads
even_thread = threading.Thread(target=even_factors, args=(number,))
odd_thread = threading.Thread(target=odd_factors, args=(number,))

# Start threads
even_thread.start()
odd_thread.start()

# Wait for both threads to finish
even_thread.join()
odd_thread.join()

print("Exit from main")

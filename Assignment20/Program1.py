"""1. Design a Python application that creates two separate threads named Even and Odd:
The Even thread should display the first 10 even numbers.
The Odd thread should display the first 10 odd numbers.
Both threads should execute independently using the threading module.
Ensure proper thread creation and execution.
"""

import threading

# The Even thread should display the first 10 even numbers.
def Even_Num():
    for i in range(2, 21, 2):
        print("Even Numbers :", i)

def Odd_Num():
    for i in range(1, 20, 2):
        print("Odd Numbers:", i)

# Create threads
even_thread = threading.Thread(target=Even_Num)
odd_thread = threading.Thread(target=Odd_Num)

# # Start threads
# even_thread.start()
# odd_thread.start()

# # Wait for both threads to finish
# even_thread.join()
# odd_thread.join()

even_thread.start()
even_thread.join()
odd_thread.start()
odd_thread.join()


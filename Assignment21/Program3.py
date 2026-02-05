"""3: Design a Python application where multiple threads update a shared variable.
Use a Lock to avoid race conditions.
Each thread should increment the shared counter multiple times.
Display the final value of the counter after all threads complete execution."""

import threading
import time

# Shared counter
counter = 0

# Create a Lock
lock = threading.Lock()

# Function for threads to increment counter
def increment(name):
    global counter
    for i in range(10):
        lock.acquire()           # Acquire lock
        counter += 1             # Increment counter
        print(f"{name} incremented counter to {counter}")
        lock.release()           # Release lock
        time.sleep(2)          # Small delay to see thread switching - 30 sec

# Create threads
t1 = threading.Thread(target=increment, args=("Thread-1",))
t2 = threading.Thread(target=increment, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

# Final counter value
print("Final value of counter:", counter)

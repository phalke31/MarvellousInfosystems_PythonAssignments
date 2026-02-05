"""2: Design a Python application that creates two threads.
Thread 1 should calculate and display the maximum element from a list.
Thread 2 should calculate and display the minimum element from the same list.
The list should be accepted from the user."""

import threading

Numbers = list(map(int, input("Enter elements : ").split()))

def Maximum_Number(Numbers):
    maximum = max(Numbers)
    print("Maximum number is : ", maximum)

def Minimum_Number(Numbers):
    minimum = min(Numbers)
    print("Minimum number is : ", minimum)

# create thread 

Maximum_thread = threading.Thread(target=Maximum_Number, args=(Numbers, ))
Minimum_thread = threading.Thread(target=Minimum_Number, args=(Numbers, ))

Maximum_thread.start()
Minimum_thread.start()

Maximum_thread.join()
Minimum_thread.join()

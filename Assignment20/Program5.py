"""5: Design a Python application that creates two threads named Thread1 and Thread2.
Thread1 should display numbers from 1 to 50.
Thread2 should display numbers from 50 to 1 in reverse order.
Ensure that:
Thread2 starts execution only after Thread1 has completed.
Use appropriate thread synchronization."""

import threading

lock = threading.Lock() # lock class

lock.acquire() # lock used outside def -- to get first thread exicuted first time and then second will exicute -- sequentially 
def Thread1():
    print("Sequence order number : ")
    for i in range(1,51):
        print(i)
    lock.release()

def Thread2():
    lock.acquire()
    print("Reverse order numbers : ")
    for i in range(50, 0, -1):
        print(i)
    lock.release()

# create threads

T1 = threading.Thread(target=Thread1)
T2 = threading.Thread(target=Thread2)

T1.start()
T2.start()

T1.join()
T2.join()
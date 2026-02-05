"""3: Design a Python application that creates two threads named EvenList and OddList.
Both threads should accept a list of integers as input.
The EvenList thread should:
Extract all even elements from the list.
Calculate and display their sum.
The OddList thread should:
Extract all odd elements from the list.
Calculate and display their sum.
Threads should run concurrently."""

import threading

# why split() function : ["10","20","30"] → then converted to → [10,20,30] -- strig to int conversion

Numbers = list(map(int, input("Enter user inputs : ").split()))

def Even_list(Numbers):
    sum = 0
    for Num in Numbers:
        if Num % 2 == 0:
            print(Num)
            sum += Num
    print("Sum of even number is : ", sum)
        
def Odd_list(Numbers):
    sum = 0
    for Num in Numbers: # finding Num inside Numbers 
        if Num % 2 != 0:
            print(Num)
            sum += Num
    print("Sum of odd number is : ", sum)

Even_list_Thread = threading.Thread(target=Even_list, args=(Numbers, ))
Odd_list_Thread = threading.Thread(target=Odd_list, args=(Numbers, ))

Even_list_Thread.start()
Odd_list_Thread.start()

Even_list_Thread.join()
Odd_list_Thread.join()

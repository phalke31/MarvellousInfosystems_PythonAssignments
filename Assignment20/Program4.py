"""4: Design a Python application that creates three threads named Small, Capital, and Digits.
All threads should accept a string as input.
The Small thread should count and display the number of lowercase characters.
The Capital thread should count and display the number of uppercase characters.
The Digits thread should count and display the number of numeric digits.
Each thread must also display:
Thread ID
Thread Name"""

import threading

String_data = input("Enter string : ")

lock = threading.Lock() #class lock

def Small(String_data):
    count = 0

    lock.acquire() # Take lock before printing
    print("Lowercase characters are : ")
    for ch in String_data:
        if "a" <= ch <= "z":
            print(ch, end=" ")
            count += 1
    print()   #  moves cursor to next line

    print("Count of small thread is : ", count) # we want total count hence written at 1 indentation
    print("Thread id : ", threading.get_ident()) # display id
    print("Thread name : ", threading.current_thread().name)
    lock.release() #  Release lock after work
    
def Capital(String_data):
    count = 0

    lock.acquire()
    print("Uppercase characters are : ") # written outside loop because we don't want to print this line repeatedly if write inside loop everytime it will display print line we need only characters to be display 
    for ch in String_data:
        if "A" <= ch <= "Z":
            print(ch,end=" ")
            count += 1
    print()   #  moves cursor to next line

    print("Count of Capital thread is : ",count)
    print("Thread id : ", threading.get_ident())
    print("Thread name : ", threading.current_thread().name)
    lock.release()
    
def Digits(String_data):
    count = 0

    lock.acquire()
    print("Nuemric digits are : ")
    for ch in String_data:
        if "0" <= ch <= "9":
            print(ch,end=" ")
            count += 1
    print()   #  moves cursor to next line

    print("Count of digits are : ",count)
    print("Thread id : ", threading.get_ident())
    print("Thread name : ", threading.current_thread().name)
    lock.release()

# Create threads 

Small_thread = threading.Thread(target=Small, args=(String_data, ), name= "Small")
Capital_thread = threading.Thread(target=Capital, args=(String_data,), name= "Capital")
Digits_Thread = threading.Thread(target=Digits, args=(String_data,),name="Digits")

# start threads
Small_thread.start()
Capital_thread.start()
Digits_Thread.start()

# wait until finish
Small_thread.join()
Capital_thread.join()
Digits_Thread.join()

    
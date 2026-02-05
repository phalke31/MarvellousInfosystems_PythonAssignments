"""4: Design an application that creates two threads.
Thread 1 should compute the sum of elements from a list.
Thread 2 should compute the product of elements from the same list.
Return the results to the main thread and display them."""

import threading

Numbers = list(map(int, input("Enter elements : ").split()))

results = {} # shared dictionary to store results of sum and product

def Sum(Numbers):
    total = 0
    for num in Numbers:
        total += num
    results['sum'] = total

def Product(Numbers):
    total = 1
    for num in Numbers:
        total *= num
    results['product'] = total


Sum_thread = threading.Thread(target=Sum, args=(Numbers, ))
Product_thread = threading.Thread(target=Product, args=(Numbers, ))

Sum_thread.start()
Product_thread.start()

Sum_thread.join()
Product_thread.join()

# main thread

print("Total sum of numbers is : ", results['sum'])
print("Total sum of product is : ", results['product'])
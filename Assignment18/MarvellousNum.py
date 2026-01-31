
def chkprime(num):

    if (num <= 1):
        return False # Not prime
    for i in range(2, num):
        if(num % i == 0):
            return False # Not prime
        return True # prime no of loop completes
    


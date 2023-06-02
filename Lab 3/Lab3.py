# Imports
import math
import time
import random

def isPrime(p):
    if p < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(p))+1):
            if (p%i) == 0:
                return False
        return True
    return False

def nBitPrime(n: int):
    my_number = 0
    while not isPrime(my_number):
        x = random.random()
        my_number = x*(2**n)
        my_number = int(my_number)
    return my_number

def generatePQ(n: int):
    P = nBitPrime(n)
    Q = nBitPrime(n)
    return P*Q

def factor(PQ: int):
    for i in range(2,PQ):
        if PQ%i == 0:
            P = i
            break
    Q = PQ / P
    return P,Q

if __name__ == "__main__": 
    n = 10
    print("N\t\tTime")
    while n <= 100:
        PQ = generatePQ(n)
        t1 = time.time()
        P,Q = factor(PQ)
        t2 = time.time()
        difftime = (t2-t1)*1000
        print("{}\t\t{:.3f}".format(n,difftime))
        if t2-t1 > 300: #t2-t1 = time difference in seconds. If this is over 300 seconds, that is higher than 5 minutes, 
                                #which is our time limit
            break
        n+=1
# After running this code, we introduced those values into Excel, 
# and then used the curve fitting feature to get the approximate function it follows. It is something like: 4E-05e^0.6721x
# With this, we get that the approximate time to crack a 1024 bit key in my laptop would be 9.9456E283 years.
# I tried to check with a 2048 bits key, and the number was so large Excel was unable to show it.


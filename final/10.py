# imports
from collections import defaultdict
def recur_fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n < 0:
        raise Exception("We need a positive integer")
    return recur_fibo(n-1) + recur_fibo(n-2) + recur_fibo(n-3)

def dinamyc_fibo(n):
    # First, we set the base cases
    res = defaultdict(int)
    res[0] = 0
    res[1] = 1
    res[2] = 1

    for i in range(3, n+1):
        res[i] = res[i-1] + res[i-2] + res[i-3]
    return res[n]

if __name__ == "__main__":
    n = 15
    print("Recursion")
    for i in range(n+1):
        print(recur_fibo(i))
    print("Dynamic Programming")
    for i in range(n+1):
        print(dinamyc_fibo(i))
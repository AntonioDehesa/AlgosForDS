# imports
from time import time
from collections import defaultdict

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
            # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
                # Keep the best
                minCoins = min(minCoins, currentMin) 
        return minCoins

# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    n = len(coins)
    # Create the initial tables
    optNum = defaultdict(int)
    actualCoins = defaultdict(list)
    # Fill in the base case(s)
    for coin in coins:
        optNum[coin] = 1
        actualCoins[coin].append(coin)
    # Fill in the rest of the table
    for i in range(n):
        coin = coins[i]
        for j in range(1,amount+1):
            if optNum[j]  == 1:
                pass # Base case
            elif j > coin:
                if (optNum[j-coin] + optNum[coin] > 0 and optNum[j-coin] + optNum[coin] < optNum[j]) or optNum[j] == 0:
                    optNum[j] = optNum[j-coin] + optNum[coin]
                    actualCoins[j] = actualCoins[j-coin] + actualCoins[coin]
    res = actualCoins[amount]
    res.sort()
    for elem in res:
        print(elem)
    return optNum[amount]#, actualCoins

C = [1,5,10,12,25] # coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))
# A = 29
assert A>=0
print("DAC:") 
t1 = time()
numCoins = DACcoins(C,A) 
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
print() 
print("DP:") 
t1 = time()
numCoins = DPcoins(C,A) 
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
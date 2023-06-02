# 1

h -> c -> b -> g -> f -> d -> a -> i -> e

In the case of F, I was unsure, as it is a constant with n. Eventually, it would be surpassed. 

# 2

## A 

O(n)

## B 

O(n^2)

## C

O(n log n)

# 3

X * (n log n) = 1
So X = 1/(n log n) where n = 1000 = 0.00033333

Then 
0.0003333 * (n log n) where n = 1,000,000 = 2000

2000

# 4

## A

Inefficient. It would be better to pop / push from the end

## B

Efficient

## C

Efficient

## D

Inefficient

## E

Efficient

# 5

## A

Stack. 

## B

Heap

## C

List

# 6

## Bubble sort

It has a best case of O(n), worst case of O(n^2), average case of O(n^2)

In the first case, the initial sort of the list, it would be an average time, O(n^2), as we know it is randomized. 

Then, once it is sorted, it would have to "invert" it, which would be a worst case scenario. 

So it would be O(n^2) + O(n^2)

But the bounds of the bubble sort would be from O(n) + O(n^2), in the case the randomized file is actually sorted from the very beginning, to the worst case in which it is reversed sorted for both cases, O(n^2) + O(n^2)

## Insert sort

Best case O(n), average O(n^2), worst O(n^2)

The times would be similar. 
With the randomized list, we would have an average case O(n^2)
Then with the already sorted list, we would have a worst case O(n^2). 

So it would be O(n^2) + O(n^2)

The bounds would be from O(n)+O(n^2) to O(n^2) + O(n^2)


## Merge sort

The best, averge and worst cases are O(n log n)
So the bounds and everything would be O(n log n) + O(n log n) = O(n log n)

# 7

## Breadth first

This algorithm first searches through all the nodes at the same level before looking at any node at the next level. 
The advantage is that it avoids going down a rabbit hole looking at infinite depth levels when the solution was in the node next door. 
For example, in algorithms to look for the best path. 

The disadvantage comes when there are a lot of nodes at the same level, and the solution might be at a deeper level. 

The pruning helps us avoid redundant node exploration. 

## Depth first

It looks first through all the possible nodes in each branch (node) before exploring the next node.
In this case, this would help us in this way: 
It explores the entire branch, and say, gets a number. 
If when exploring the next branch, the number is worse than the number from the other bracnh, either larger or smaller, we can stop the exploration and prune the rest of the branch. 


## Best first search

It explores the most promising node first. What most promising means depends on what our goal is. 

The pruning for BFS is helpful to avoid visiting a node twice. We keep a record of visited nodes to avoid duplicate work. 
Similar to breadth first search. 

We could also simply prune nodes that are not promising at all, but this would have the disadvantage of possibly deleting a node that has children node that are more promising than the other nodes. 

# 8

## a

Incremental design

## b 

DAC

## c

Backtracking, DP and Greedy work. But greedy might be the best, as we could use the Knapsack problem as a basis

## d

Backtracking, DP and Greedy work. But backtracking might be better, as we have solved a similar problem in the past. 
But honestly, this problem could be solved simply by sorting the items and adding items with the lowest weight into the backpack, as many
as possible, like incremental design. 

# 9

Similarities: Dynamic programming has been described as divide and conquer with memory. 
Both break a big problem into multiple smaller problems. 
Both detect repeated subproblems, and store them for future use. 
Both use [optimal substructure], which is that the optimal solution for the problem is made up of optimal solutions of the subproblems

Differences: 
DAC just breaks down the problem in multiple subproblems, while DP solves the problem from the simplest subproblem building up to more complex subproblems
In DAC, each subproblem is completely independent, and solved indepdendently even if it has been solved before. While DP knows if it has been solved before, and skips it. Also, in DP, the subproblems add up to a bigger subproblem, while in DAC they are completely independent. 

I would use DP when the subproblems overlap and can support each other to get the solution for a bigger subproblem. 

# 10

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
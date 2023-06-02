# Hash tables

In python, dictionaries and sets use hash tables. 
Its a list of size m that maps objeects in an immutable universe U to a position in the list. 
They have to be one to one, and avoid collisions. 
Direct addressing is rarely used, as it would create a massively large list. 
But a smaller table increase the chance of collision. 

## Hash functions
### Division method
h(k) = k mod m

If k consists of many digits, it can be interpreted as a r+1 digit number in base b. 

h(k) = (sum from i = 0 to r of k_i * b^i) mod m

### Multiplication method

h(k) = floor(m(k*A mod 1))



It is technically impossible to get 0% collisions in every key. 
It may or may not happen if abs(K) <= m
but it will definitely happen if abs(K) > m

If can be solved by:
if a collision is found, look for a different slot (open addressing)
chaining (store all objects with the same hash in another table)

#### Chaining
good performance is guaranteed if the lists are short
in the worst case, everything maps to the same slot, which would just be a list


#### Open Addressing

store all keys in the hash table itself. 
each slot contains either a key or a none

# Data Structure Selection

The more restrictive the set of operations, the faster the implementation. 

## Lists

Lists are the most general in terms of operations
• Every element can be accessed in any order
• Can do anything with a list. Just not always fast
• O(1) if we know the index of the element we want
• Slower runtimes if we need to
    • Maintain a particular ordering
    • Rearrange elements
    • Search for a particular target element
    • Search for an element meeting a property (maximum)

## Stacks and Queues

* Stacks and queues restrict which elements you
can access
    • The first and last elements
• Input ordering is maintained when output
• O(1) to insert or remove elements
• Not possible to:
    • Rearrange elements
    • Search for a particular target element
    • Search for an element meeting a property (maximum)

## Heaps

* Heaps only allow you to remove the elements in
order
    • Biggest first (maxHeap) or smallest first (minHeap)
• No indexed access
• Input order is not maintained
• Only useful for keeping a sorted list
• O(log n) to remove the top element or add
element
    • Runtime to maintain a sorted list with an actual list
    is slower


## Hash tables

Hash tables give fast access for lookup
operations
    • Example: Find the phone number for a given name.
• No indexed access
• Input order is not maintained
• Sorted order is not maintained
• O(1) lookup and insertion
    • Runtime to do lookup with an actual list is slower.


## Hybrid structures

Sometimes we need special structures that require two fast operations, or a special function, so we might have to combine them. 
For example, to get fast look-up times, we may need a hash table, but to also maintain the input order, we may need a linked list. 
So we create a custom structure to do both. 

# Graph Search

Both keep a data structure D of pending edges to explore and repeatedly choose an edge from D to explore. 
Both are linear. 
Both have the same code and algorithm, but the difference is only in the data structure that you use. 
## Breadth first search
Uses a queue
## Depth first search
Uses a stack
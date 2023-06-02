# Abstract Data Types (ADT)

Set of values (represented by a model) and a set of operations (methods) that can be performed on those values. 
Abstract because it separates the specification (what you can do with it) from the implementation (how the objects are represented with state variables and how the operations realize the desired behavior).

They consist of two components: 
## Public
AKA external portion. 
* A conceptual or users view of what the objects look like
* The method or conceptual operations available to the users of the type

## Private
AKA Internal portion

* The object representation or state
* The implementation of the public methods
* The implementation of some internal methods

## Methods

The usually fall in one of the next categories: 
* Initialization
* State changing
* Access
* Destruction

## Data Structure

It´s a policy for storing a collection of data values in compute memory with the goal of supporting a specific set of operations efficiently.
Used to implement an ADT. 
The ADT defines the logical form of the data, and the data structure represents the physical form via state variables. 

## Examples
### Stack

Dynamic set. LIFO. 

### Queue

Dynamicset. FIFO.

## Implementing ADTs

In python, it is with [class] type.

# Stacks

LIFO.
Most popular way to implement them is using lists. 
Two ways to push/pop:
* Rear
* Front

## Rear
The first element to be added is put in the index 0, then the second element in index 1, and so on. 
Then, once poped, the element to be poped is the last element to be added in the furthest index.

O(1) complexity

## Front

It pushes the first element in the index 0. The next element to be added gets put in index 0 and the previous element gets moved to index 1. The next element would push both further away. 
Then once poped, the element in index 0 would be poped, and the rest of them would be moved one index to the left. 

O(n) complexity

# Queues

FIFO

Ways to implement them: 
## A basic list

With a list, the first element gets put in index 0. the next element gets in index 0, and the first element gets moved to index 1. etc. a FIFO

Dequeueing would remote the element in the highest possible index. 

## A circular list

A better way would be to use a circular list. 
We could use two indexes, H and T, heads and tails, to know where the head, first element, is, and the tail, last element, is. 

A 1 element queue would have the H and T in the same index. 
When dequeueing, we could just remove the element in the first index, and move the heads further up the index. 

You can also do it without a list, just nodes. Each node has the data, and a pointer to the next node. 
dequeueing just deletes that node, and the head is the one that the poped element was pointing to. 
## A doubly linked list

This one does not require a list itself, we can just create nodes, which point to the next and the previous one. 

## Efficiency
* list: O(n) enqueue, O(1) dequeue
* Circular list: O(1) for both
* Doubly linked list: O(1) for both

# Priority Queues

A queue where you can cut in line. 
It requires these operations: 
* insert
* max: return the maximum of s
* extractmax: remove the maximum of s

extractmax would actually remove the element with the highest priority. as a regular pop. 

Applications: 
task scheduling, simulation, greedy algorithms, Huffman coding, etc. 

To do this in an efficient way, we use a binary heap. 
A heap is a rooted binary tree with two properties:
## Structural property
Almost complete binary tree: it fills from top to bottom, and ata each level, from left to right

## Order or Heap property
H(parent(v)) >= H(v) for all nodes V

## Heap insertion and removal

### Insertion

O(log_2 n)

### Removal

only allowed to remove the maximum element

cant leave an open hole at the root, so the last element moves to the head. 
but then, the last priority would probably make it so the heap is not fulfilling the first characteristic. So we would swap it with one of the children. 
And so on and so forth until it gets to its right place. 
But honestly, would it not be better to swap the original head with the largest child, and so on and so forth? 
O(log_2 n)

## Heap sort

just a binary tree

to build the heap:
O(n log_2 n)

to output the elements in descending order:
O (log_2 n)

quicksort is usually faster than heapsort. 

total time: 
O(n log_2 n)
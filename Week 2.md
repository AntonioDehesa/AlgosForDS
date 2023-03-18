# Small World Problem

It comes from "Its such a small world". It is the conceptual idea on how far apart are two random individuals. 
The simplest example is the six degrees of separation. We all know each other in the world through six people. I know someone, they someone, and so on, so we are all connected. 

Other examples: 
* how many steps im away fron an actor, or a doctor

Its useful for disease spreading, Facebook information spreading, etc. 
To see if a group is a "small world", in which everything spreads quickly, or not. 

To do this with an algorithm, you need a mathematical model. For this, we need a graph. 
A non-directional graph. 

And what we really want to do is build up a distribution of statistical properties on, as I say here, pairwise shortest path lengths. So what do I mean by that, OK? What I want to know is-- how many people are connected to other people with one step? How many people are connected to other people with two steps, and then three steps, and then four steps?

And so the idea would be I want some sort of distribution. So if I run this analysis, and 70% of the people are connected with one step in whatever network I'm looking at, and another 20% of the people are connected in two steps, and the rest of them are connected in three steps, then that is a really small-world problem because that's a really small, interconnected group because they're connected so tightly. And so any rumors, or diseases, and stuff like that are going to spread really, really fast.

If I did that analysis, and I found out that very few people- 10%, 20%-- are connected with one or two, but I have a larger percentage that are connected at six or seven or eight steps from each other on average, then things are not going to spread quite so fast. And that would impact my analysis.

Special cases: if our graph is not connected. It means they dont know each other. That would affect our real life model, but we wont actually look at this special case when implementing it. 

So our SWP algorithm takes a graph as an input, and outputs the distribution of distances between all pairs of nodes. 

Basically, we just need to find the distance (minimum distance) between nodes. 

You cant really brute force it, as it depends on the size of the graph, or the adjacency matrix, and it uses an algorithm of the size. 

## Queues

Instead of brute forcing it, we can use queues. 
Our brute force algorithm does this: 
it considered all paths in order of increasing lengths. So what we did was we first looked at, is there a path of length 1? If there wasn't, then we said, OK, is there a path of length 2? And if there wasn't, then we said, is there a path of length 3?

And one of the things that we didn't do particularly well, and one of the reasons why this was so slow, is that what we ended up doing was we ended up recreating those all the time. We went from paths of length 1, and then we just forgot all about that. And then we did paths of length 2, and then we forgot all of that. And then we did paths of length 3, and then we forgot all that.


Using queues, instead of recreating the paths each time, you save them, and build on top of them. 
In exchange, you are using more memory. 
Queues are FIFO. 

### Breadh-first search

What we need to do is visit all ndoes in the graph, looking through the edges. We are visiting in a particular order. 
It explores the graph starting at a source node. Then its going to visit each neighbor. and for each neighbor, we are visiting their neighbors, and so on. 
We use queues to guarantee that first we visit all the neighbor nodes before any neighbor node of those neighbors. 
All nodes at level i appear earlier in the queue than any node at leverl i+1.

# Paradigms

A pattern to perform an action that has been tried and was been successful. 

For programming, we have design paradigms for our algorithms. 
That way, we can split our problem-solving techniques in categories, and that way, we can reuse code or approaches. 

That way, we can also have an expectation on the efficiency of the code or implementation we are using. 

Examples of these techniques: 
* Brute force
* incremenetal
* divide and conquer
* decrease and conquer
* randomization
* iterative improvement
* backtracking
* branch and bound
* dynamic programming
* greedy solutions
* approximation

## Incremental design

We build things up incrementally. 
Our example is sorting.
First, sorting, in a very mathematical definition, is: you have a sequence of values taken in some domain, and you produce a permutation of those values, such that they are in order. 
What "order" means is up to you: directly, reverse, by characters, by distance, etc. 

In incremental design, you work in small steps.
In DS, you may not have all your data at once. So you solve the first part of your data, and once more data arrives, you just incorporate it to the previous solution. That way, you do not have to start all over. 
Similar with sorting. Once you have a sorted list, if you add new elements, you just have to sort that one element, and not the entire list again. 

## Divide and Conquer: DAC

As its name describes. 
There are 3 steps to divide and conquer:
* Divide: We divide the problem into smaller pieces
If we have, say, 10000 items, we can divide it into multiple fragments, and work with, say, 10 sets of 1000. The division could be with a central element to compare to: Anything larger than this goes into this set, anything smaller goes into this other set
* Conquer: We solve the problem. In this case, we could sort each of the 1000. 
* Combine: We combine the already sorted elements. 

Remember: not every problem can be divided.

# Sorting efficiency

Things like insertion sort or selection sort are not very efficient, so we could use merge sort. 

## Merge Sort

We take our list to sort. We split it by the middle. Then, we sort both halves applying merge sort to each again, and merge them again. DAC. 

Accessing an arbitrary element of a list takes O(1) time.
Complexity is T(n) = 2*T(n/2) + n (for n >= 2)

that  + n comes from the merging back step. 
Big O: O(n log n)
Much faster than insertion or selection sort. 
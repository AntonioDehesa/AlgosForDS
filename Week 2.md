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


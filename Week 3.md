# Introduction to Efficiency

What makes a good program: 
* It works as specified
* It is easy to understand and modify:
    * Decomposition: you can break your code into pieces so you can tackle each piece one at a time
    * Abstraction: Separate the interface from the implementation details. Hide background details or any unnecessary implementation from the data
    * Generalization: Design functions that have a good chance of being reused elsewhere
* It is reasonably efficient in time and memory. For our purposes, mainly time. 
What reasonable means depends on the application. 

There are a lot of questions to ask: 
where is it running (hardware and software)
what are the inputs
how many
what is quick in our settings
how it compares to other algorithms

Now, how do we measure efficiency? We will use costs, and for the example, the algorithm for insertion sort.

for i in range(1,len(L)):                   # c1n
        key = L[i]                          # c2(n-1)
        j = i-1                             # c3(n-1)
        while j>= 0 and L[j] > key:         # c4 sum ot t_j from j = 2 to n
            L[j+1] = L[j]                   # c5 sum ot (t_j-1) from j = 2 to n
            j = j-1                         # c6 sum ot (t_j-1) from j = 2 to n
        L[j+1] = key                        # c7(n-1)

Each of the cs is a constant. We do not know how long it will take to run on our system, but whatever takes, will happen n times, or n-1, or sum ot (t_j-1) from j = 2 to n times.
The t_j means, basically, we dont really know how long it will take, as for this algorithm, we may be forced to go back to the beginning with each iteration. 
So the final complexity is: 
T(n) = an + b(sum ot (t_j) from j = 2 to n) + c

## Best, Worst, Average Efficiency

We had a first attempt previously at defining efficiency, and one of the downfalls is that it didn't really capture the essence of making our thing machine-independent. And so we kind of walked through that, we noticed those constants were machine-dependent, and that wasn't really a good thing.

And so we have a second attempt right here that we're going to say, if an algorithm is efficient, if, when implemented on any computer and in any language, it performs a small number of basic steps on real input instances, OK? So we're trying to take the computer out of the equation and focusing on these basic steps.

Now, what are these basic steps? These basic steps are just going to be sets of instructions that take some constant amount of time to be executed, OK? It may take half a second on my machine. It may take a quarter of a second on another machine. The fact that it takes a slightly different on each machine is unimportant. What's important is that it's a constant time relative to the input size.

So al algorithm is better if it performs fewer basic steps. 
Going back to insertion sort, we will look for best, worst, and average run times. 

For some cases, best, average, and worst are the same. 

An exact analysis is difficult, as can be best, worst, and average. 
An algorithm is efficient if, for large inputs, it performs significantly fewer basic steps than a brute force approach. 

# Algorithm efficiency part II

## Efficiency bounds

Previously, we discussed that in algorithms we could ignore the lower order terms, as when we scale, only the highest order term matters. 
However, an easier approach to this is using bounds. 
For most purposes, it is not so important that we get a very very specific efficiency, as long as our efficiency is bounded from the top and / or the bottom.

These bounds are usually functions, which the larger the input, the higher the efficiency in terms of execution time. 
So we dont have a specific efficiency, but we can guarantee that its between two functions / values. 

### Symbology: 

* O: Big O. It represents an upper bound
* Omega : Big Omega. Represents a lower bound. 
* Theta: Big Theta. It describes both the O and Omega for a code

Now, the limits dont always have to be bigger or smaller than the function. As long as after some time has passed, the limit will be either bigger or smaller. 

## Example

### Insertion sort
So insertion sort is
(a1 + a2)n + a3 -1 <= T(n) < a1n + a2*((n+2)(n-1))/2  + a3
So 
if we ignore constants:
n <= T(n) < n^2
So T(n) E omega(n) and T(n) E O(n^2)

Now, the upper bound may be deceiving.
A function that has a runtime of n, it would be valid to say it has a big O of O(n), or O(n^2), or O(n^3), as n is < n^2 and n^3

Adding and multiplication of functions apply. 
Meaning, if code A with O(n) runs inside of code B with O(n^2) then the result would be O(n^3) as any time code B runs, code A with execute O(n).

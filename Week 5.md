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


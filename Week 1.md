# Introduction to algorithms

Data Science is a mix between computer science topics, like parallel programming, databases, programming in general. Statistics play big roles in things like data mining, stuff like that, and then often some other specific domain of studies, like finance, health, etc. 

We are focusing on the computer science aspect of it, worrying about teaching a few core computer science topics to sort of help cover this portion a little bit. And then there's obviously other classes you're taking for statistics and stuff like that, where you get some of the other pieces.

## Big Data
Its a term that's thrown around all the time. But it really means big data. We are collecting more and more data than we ever have. 

So the idea is we are collecting data all the time. And we need to worry about what we're going to do with that data. And this is sort of a key moment here for a lot of things is, data are not information. Just because you collect lots of data doesn't mean you have good information to make business decisions or make a scientific calculation on something. It is just data.

We need to figure out how to turn all of that data into information. And algorithms are one of the things that we do for that. It helps do the processing of the data. For Big Data, we need efficient algorithms. 

So when we're actually taking a look at this, algorithmics, algorithm thing, algorithm design, as I mentioned before, it's a core technology to computing in general, data science in particular, because of the efficiency. 

There's other things as well that affect things nowadays. So certain things within computers, pipelining, caching systems, those have all gotten better over time. Parallel processing is huge in particular things like GPUs, so graphics processors can do amazing things. And so can a distributed computation, where we've got a bunch of different computers sort of cloud computing type stuff, where you have a bunch of computers that are all working on processes at the same time. So GPUs, these graphic processors, are very fast on one machine. These can be very fast if you use something like a Hadoop or MapReduce, or Spark is one of the latest, greatest things that people are using to do this sort of distributed processing.

These things are all important, too. And we actually have other courses that talk about these things. So we're going to not spend a lot of time in this class talking about the sort of distributed processing stuff, because we're going to focus on sort of one machine, the core ideas of efficiency, and try to get that sort of baseline down so you understand the language that we're talking about with it and understand what we're doing with the basic stuff. And then when you get into other courses that deal with some of the parallel stuff, you'll learn how to expand that to some of the other parallel processing stuff.

Algorithms are used for solving all sorts of problems. 
So things like this, finding optimal paths. We've all done the mapping stuff on our phones, where I want to go from home to work, for example, and I want to do it in the shortest time possible. T
It's not just those routing things that are not just the shortest path in a road network, but how do the packets on the internet-- you are viewing this over the internet right now. This video is getting broken into millions of little packets and sent across the internet to you in little pieces and routed all through the system and reappearing on your computer in the right order. How is that happening? So that's happening with an algorithm. Places like UPS and FedEx, they route their shipments using routing algorithms as well. So we'll look at some of these routing algorithms as we go through.

You've all used search engines, so searching and indexing. 

Data compression-- that's one we don't often think about, but every time you do anything-- a lot of us have taken a file and zipped it up and unzipped it. That's compressing it. But anytime you've used a video, an audio file, or an image, you are compressing stuff. And so certain types of files, we need lossless compression. So for a text file, when we compress it and then we uncompressed it later, we want it to look exactly the same. We don't want an A to be changing to a Q. That would not be a good idea.

But lots of other types of compression use what we call lossy compression. So all the videos that you watch for the most part, all those music things that you listen to, those are all compressed in the sense that they're lossy compression. And when it actually compresses it to take less space to send across the internet or to store on your file system, it's actually throwing away information it doesn't think your eyes or ears will notice. And they do a really good job with that sort of stuff. And so there are algorithms to do that sort of stuff.

So whether it's a Java program or a Python program or a C++ program, wouldn't it be great-- and you guys have written enough code in a couple of your other classes to know that you could happen to write loops that are wrong. And if you code a loop that's wrong, it might run forever. It would be awesome if we could run some sort of algorithm that checked our code to see if there were going to be any issues like that with it before we actually put it out into production. So there's algorithms to do that sort of stuff.

There are all sorts of optimization algorithms out there as well. This is a type of algorithm we're going to be talking actually extensively about as we proceed through the quarter. And the idea is it's not just a solution to something, but you want to find the best solution to something. So I'm not just looking for scheduling a bunch of planes. I'm looking for, what's the best way of doing it? What's the least cost way of doing it? And so there's countless examples of algorithms that do that sort of stuff. So we'll talk more about optimization problems quite a lot.

Data reduction's actually pretty big for data science as well. We have mass amounts of data that we're collecting. You usually can't end up wanting your code on all of that data, or at least your really intensive algorithm on all that data. So often, we need to somehow filter that data in a little bit to give us a smaller amount of data that's still as meaningful to run the algorithm on as other types of data. So you even have these pre-processing types of algorithms out there to filter your data first.

And then, of course, we've got your standard model fitting type algorithms, where you've got things like, for example, the price history of a stock. And I know where it's been in the past, like up here in the corner right here. I know where it's been in the past, and I want some sort of estimate of maybe where it's going. Those are sort of self-explanatory for why we might want those sort of algorithms. But we have all of those pieces.

We want to familiarize ourselves with a few important algorithm types, some data structure types, and learn some algorithm design. So this is like learning the language of this. So when you're reading something and they're like, hey, I programmed this with a greedy method or I programmed this with backtracking, you'll actually know what they're talking about. You'll know what the general efficiency is of it. You'll know if it's applicable for the type of problem that you're trying to adapt it to. And so we're going to learn the languages of what those things are.

We're going to learn how to predict performance for things, to see, hey, even before I code this algorithm up, if I wrote this and my data set expanded, is this actually going to scale up efficiently? And again, that kind of ties with this. There are certain types of things that it just doesn't matter what you do. They just are hard to compute. And nobody's found a good way to do this yet. And that's something else that we can get a better understanding of by looking at algorithms.


## What is an Algorithm

It's an abstraction of a computer program.

It's some sort of a finite procedure that's going to take in a bunch of input and in a set amount of time produce some output
That's about as abstract as it can get. This finite sequence of instructions is going to be expressed in some language. 

And we must solve a general problem. So there's going to be restrictions. So obviously, this input that's coming in, you can't just produce any output. You have to take that input and follow some rules to produce some sort of output. So sorting, for example, takes in any sort of list of items, and does some processing, and in a finite amount of time produces some output, which happens to meet some rules, like every element is smaller than the element in front of it. 

### Important bits
* Finite time: Preferably a short time. Just because its finite, does not mean its useful for us. 3 centuries is finite, but 
* Takes an input: Within some constraints, it should be able to take any input. Not just some very specific values. 
* Expressed in some language: Not a programming language, but a human language. It needs to be expressed in, for example, plain english, and with a model first before it gets put into code. You can't code something that you don't understand conceptually.

### What defines a good algorithm
* Correctness: It may be very fast, but it is useless if it does not produce the right answers. Correct in every situation, not just specific ones. It cant either just be the right answer. It needs to be the right answer for our purposes. I don't want to walk from New York City to LA. I mean, I could get there. I'd rather fly from New York City to LA, OK? It's a faster approach, even though walking would get me there.
* Efficiency: Fast algorithms that use as little memory as possible. 
* Ease of implementation: If the above are met, then we will choose the algorithm that is easier to implement and use. 

### Algorith design

Algorithm design paradigms and data structures.
Algorithm design paradigms right here, these are techniques, standard techniques, that we can use to solve problems, right?

You have a new problem that comes up. You do not have to invent reinvent the wheel every time you see that problem. You'll be like, oh, this is one of these types of problems. And I've learned these five standard ways of solving things. This problem fits into one of these categories. And so I can use these techniques that I learned to do it more efficiently.

Same thing with data structures. We're going to talk about some data structures as well. We don't just want to take everything and, for example, in Python, and throw it into a list. We don't get particularly good, efficient algorithms that way. So we talk about a number of different data structures that are available to us to actually hold data. And we talk about their efficiency so you can better choose which one it is that you want to actually use.

And then we'll obviously be talking about running time costs when we talk about efficiency. Certain types of algorithms just take way too long to compute. And often, they're the algorithms we come up with first, right? I mean, it's oh, yeah, this is the-- oh, yeah, I understand how to solve that problem. This is my solution. It's the first one you think of.

And you start coding it up. And then you realize, oh, it works when I have 10 numbers. But my data set has a million members. And it doesn't scale well. And so those are the things that we need to end up thinking about with efficiency.

So when we're actually coding our algorithms right here, there's a couple of main things we need to worry about. I already talked about correctness earlier a little bit. It must produce the correct output for everything, right? It's not enough just to test your algorithm on a few instances. You need to extensively test it on lots of stuff.

So a mathematician would probably tell you you probably need to prove that it works in every case. Computer scientists tend to be a little more lax that way. And we tend to just traditionally sort of test our programs, and test it on a bunch of cases, and hope it works. And the problem with that, of course, is you get software bugs sometimes after it's been released. Then you just roll out a bug fix. And it's fine.

Those sort of days are ending as we're getting more and more software that's controlling medical equipment, and cars, and airplanes. You don't just want a bug to occur and roll out a bug fix after a couple of cars have crashed. It's more imperative than ever now to actually make sure that our code, our algorithms we're working on, are really, truly working in all cases.

Efficiency is very important. Both in memory and speed. We usually trade memory efficiency for more speed, but sometimes, for some devices, this is not possible. 

And all things being equal, we would rather have algorithms that are easier to implement. We're going to find that most of the time, all things are not equal. And often, one algorithm is more efficient than another one. And that's when we're going to end up choosing.

But if you've got a couple of choices, you'll go for the easier to implement one. It's less prone to errors. And it would be great if we could have our algorithm be as general purpose as possible so that we could use it in other circumstances as well and not just the particular problem we're trying to solve at that moment.

These are the things that we're going to do when we're trying to solve our problems. First thing we have to do is really actually understand what the problem even is, right? What's available for data? What's the desired output? What are the special cases that come up? What are some of the things that you're assuming? Clients have been working in this field so long that, like if I go to a financial planner, I want to look at some sort of wealth management thing and some stock market analysis. They're so used to these assumptions that they may not tell you that sort of stuff when you're working with that data.

And so coming up with those special cases and figuring out what their assumptions are, that's really important because it sometimes just has minor impact on our algorithms, like little special cases we have to code. And sometimes it has major impact, right? Oh, if you have these things, you can't do this simple algorithm. You have to do this more complicated one that takes more time. So those are important things to figure out early.

One of the other big things that we have to do is then formulate a model for how we're going to do it. Now that I understand the problem, I'm not going to start coding right away. I'm going to construct a model with trees, or graphs, or something like that that isn't really programming, but it's more mathematical in nature to build a model for how I want to handle this.

And then we go ahead and design our algorithm that works on our model, OK? We'll talk a lot about algorithm design techniques. We'll talk a lot about data structures. And these are the things that we are going to be talking a lot about in this course to design our solution.

And then finally, we'll actually put this into code. 
Before that, pseudocode

#### How to write good pseudocode
1. Aim for clarity and precision
2. Avoid the urge to describe repeated operations informally
3. Use the constructs of programming languages to reflect the structure of the algorithm (loops, conditionals, etc.)
4. Use indentation carefully and consistently
5. Use mnemonic names. Never pronouns. 
6. Write individual steps using a human language, standard mathematical notation, or a combination
7. Avoid math notation if a human language is clearer
8. Use one statement or structuring element per line
9. Font should enhance structure and functionality

# Introduction to Efficiency

We have limited resources. We have a limited amount of time we can get things done. And we have a limited amount of space that we might be able to use in terms of memory.

Because of these limits, we need to make sure that the things we're doing are either fast in speed, or efficient in memory usage. And that's what we want to worry about.

But speed or space are machine language: they depend on system (windows, mac, linux), programming language, and insfrastructure. 

So you can write for any type of machine, any type of language, and you can code it any number of ways. And you will get different memory usages. You will get different runtimes.

So measuring efficiency is really important for big data, for data science. Because as I said, we're going to have lots of data. And before we start coding anything, I want to make sure that I can do it efficiently, that it scales well.

But because people are going to be running it on different types of machines and possibly doing it in different types of languages. How do you even measure efficiency?

I can't just say, I ran it on this machine, and it took 15 seconds. Or I ran it on this machine, it took 10 seconds. That's a meaningless number to you in the sense that when you run it, it might take half a second on your machine, or it might take eight minutes on your machine.

And so what we're going to be talking about a lot is we're going to be talking about expressing efficiency in terms of a mathematical expression, in terms of the input size. 

And then what we're really concerned about right here is we would like to choose among different algorithms before the implementation. I would really like to sort of analyze the idea of my algorithm, and sort of mathematically look at it, and decide what it's going to do and how it's going to scale before I code it up.

In data science, we use matrices a lot to hold our information. And a lot of processing on matrices involves multiplying two matrices together. So just as an example, if I have two matrices, I'm going to call them A and B, right here. So I've got matrix A times matrix B. That's going to produce matrix C.

So you're going to write an algorithm that has a couple loops.

So there's nothing fancy about this algorithm. It's something you probably have done before. But what we're really concerned about with this is, how many operations are actually performed on this?

So in particular, in this scenario, I kind of want to look at maybe how many, for example, multiplications I'm doing. Because there seemed to be a lot of multiplications, and that's a pretty expensive operation. So I'm going to kind of judge this on how many multiplications I'm having.

So it's basically, how many times am I running this line.

Once we know that, to look for efficiency, we would ask: is there something better than running this line this many times? 

# Friendship example

Modeling is a very important skill for an algorithm designer. It's obviously one of the more important skills when you're actually designing an algorithm.
It is the art of abstracting away all those messy details that both the real world has and that our implementation might have.

And so we need to think about what we're getting-- this problem that we want to solve. There's all these nitty gritty little details. We need to step above that, abstract it away, and figure out what it is that-- what the problem is that we're really trying to solve. What's the model that we're going to build for these things? And then that model is going to help us then develop the algorithm to solve this thing.

It doesn't really have to do with real world data. So if clients would come to you, they're going to tend to not have a model. They're going to tend to have real data. They're going to be like, hey, we collected all this data. I would like to analyze it for this. And so one of the first things you do is you're going to have to kind of take a look at what they're trying to do and extract some sort of model out of that data and then figure out how to use that to develop your algorithmic solution for that.

Even if you just want to use the sorting algorithm implemented in Python, you still need to model your program before choosing the right algorithm to use, because sometimes the Python algorithms don't actually match what you need.

Our models aren't going to deal with web pages and accounts. They're going to deal with other things,and like mathematical type things. Algorithmic solutions deal with low level things like coding stuff. And so what we want is something in between. Our models need to deal with things like graphs and sets and abstract data structures. And so this is the sort of thing that spans the difference between coding for loops and you know, accounts in the real world. We have to have these mathematical ideas for modeling things.

So graphs, in particular, are a big one for us. There's a lot of little ones we'll kind of learn along the way. But graphs we kind of use throughout the entire course. 

## Example: Transitive Nature of Friends

We might have somebody that's interested in mining social networks for some sort of information. So what I might want to do is consider transitive nature of friends.

So I might want to say, hey, I've got a bunch of Facebook data that I have downloaded from their API. And I want to see, hey, how likely is it that if x is a friend of z, whenever x was a friend of y and y is a friend of z. So I have a friend, Riley. And Riley has a friend, Nolan. Am I Nolan's friend, as well? You can imagine there be possible advertising revenue, other things that we could do. We could suggest that I became a friend with Nolan. So there's suggestive sell. There's advertising revenue. There's all sorts of things that you could do if you knew that sort of information.

And so we, again, need to model this. This is what they're asking us to do. And this is kind of almost written in a little bit of a mathematical language right here already, because we're talking about transitivity. But it's not modeling our data. I have a bunch of Facebook data in some form. I need to think about how I want to solve this.

And I don't want to think about the low levels of that Facebook data. What I want to think about is mathematically modeling wise how do I solve this problem. So I need to figure out how to take that data, put it into a generic style model so that I can then think about how I want to solve it. And then once I get to that point, then I can start coding it.

And so those are the steps that we need. And so modeling is really an important step. And we have this whole lecture on it right here specifically to emphasize that it's important. We're going to be modeling throughout the entire course. And I'm just going to be kind of doing it in the process of doing other things. But I do want to point out very specifically it is a important step. And a lot of people do try to skip it and jump right to the coding a lot. And we want to make sure that we definitely get that model in place.

# Graph Models

Modeling is a very important first step in understanding how to write algorithms because we have to be able to model our data that we're getting in, and then we develop algorithms based off of that. So graph models tend to be a big one that we use, and they tend to be things that, if you haven't done anything with graphs and a little bit, you tend to forget some of the terminology. 

So we have looked at a couple of previous examples in a previous lecture. One of them was a sensor network, where we had a bunch of sensors that could sense up to a certain radius and talk to other sensors within a certain radius. And we wanted to figure out, hey, can they actually talk to each other, can they actually communicate with each other, or do I have to place one of my sensors in a different location for them to actually send information all the way across to fully track somebody?

And so one of the things that we could end up doing is we could implement this with graphs. And so if you actually take a look at my sensor networks right here, I might have this sensor right here that has this radius and this sensor network right here that has this other radius right here. And since these two radii overlap with each other, what I could do is I could build a graph. And I could make where the locations of my sensors are be these nodes of a graph, and I could make the edges across the connections be the edges.

So if these sensor networks overlap, they can talk to each other. This sensor network and this sensor network overlap, they can talk to each other. And so the idea would be you could build up a graph that sort of described the connectivity of your sensor networks. And then once this graph was built up, you wouldn't need to have all these concentric circles all over the place.

You could just have the locations and the connectivity. And that would allow you to talk about, is it a connected graph, or is it two pieces that aren't connected and I need to do something to connect it, or now that I know it's connected and I want to send information from one to the next, how do I do that? How do I communicate from this one down to this one? Who do I have to talk to? Because I can't send it directly to that sensor. I have to send it indirectly through other pieces.

So this graph idea, it's a pretty powerful idea. And we're doing that all the time, where we're taking the input we have, and we might build up some sort of graph that describes my network. Now, this one was fairly easy to put it into graph form because it's this physical arrangement, right? We have sensor networks physically at various spots, and you can think about that is a physical graph.

The other example that we did was the one with the Facebook data that I had introduced, where I wanted to know if friends are you know transitive, right? If I'm friends with Riley and Riley's friends with Nolan, am I friends with Nolan too, right? Now, that doesn't sound, at least on the surface, like it would be obvious, I want to do a graph with that. Because transitivity is kind of described mathematically. And you're not thinking graphs because you tend to think graphs when you think geometrically like you would with a sensor network.

But you can do this very easily with graphs. You can actually create nodes for each person. And they're not physically in these locations, but they're just nodes between them. And then what you would do is you could actually create links or edges between two people if they happen to be friends. So if I'm friends with Riley and Riley's friends with Nolan, am I friends with Nolan too? If this was me and this was Riley and Nolan, then the answer would be I am not, in that particular case.

And so you can use this graph idea to model all sorts of things. And I'm not saying that graphs are the only way to model any of these things. It's just a very common model. and it's a model that some people don't necessarily always think about, and it's a model that we're going to be using a lot in this class to do various things.

So now that we have sort of the idea that I can take my data and maybe put it into graph models as a modeling technique, let's spend some time talking about graph basics. And I'm sure, at some point, you learned all sorts of things about graphs. A lot of these concepts are probably familiar. But it may be last week you heard about them or it may be several years ago you heard about them, so we're going to go through and talk about a bunch of terms right here so that we can get familiar with graphs again so that we can use them more easily.

And again, I kind of mentioned this right here. We have more than just those two problems. All sorts of problems can be done, right? So mathematical things like relations can be done with graphs. I showed you an example of that with a friends. Biological structures can be done-- so an example of something like this. We often do think about graphs for things like those molecules and stuff like that.

World Wide Web stuff, right? The web is connected together in various ways, and so that can be modeled as a graph. Subway and road maps, OK? We're used to kind of looking at a picture of a map and not thinking about, oh, I've got locations like street corners and I've got roads that connect them, or I've got subway stops and train things that connect them. We tend to think more about them for subways and mass transit because we tend to see the map drawn out as a graph a lot, but you tend not to think about it as much for road maps.

But that's exactly what they're modeling it as when they're doing things on all those mapping applications you have on your phone, is they're turning that pretty map you're seeing into a graph behind the scenes and doing all their algorithmic computation on that graph. Social networks, we talked about that a little bit. Polygonal meshes. So things like this little dolphin right here, this is a graphic thing. It's really just a graph as well, in terms of doing stuff. But just tons and tons of things that we can end up turning into graphs.

So onto the definitions here. So a graph has two pieces, OK? It's got vertices, and it's got edges. Sometimes I'm going to call the vertices nodes, but I'll kind of go back and forth with that. But we almost always mathematically call them vertices. And whenever you see the term v when you're talking about graphs, v is referring to the vertices, OK? And oftentimes, with the mathematical notation, when you see a capital V, it tends to mean a set of vertices. When you see a capital E, it tends to mean a set of edges that connect those two vertices together.

You see definitions like this all the time. E is a finite multiset of pairs from V cross V. What does that mean? It means, basically, it's a pair of vertices, right? I'm going to go from vertex A to vertex B, so the edge is going to be something that represents vertex A to vertex B, OK? And so that's just how you read some of that mathematical notation, and we need both vertices and edges to actually form our graph.

We talk a lot about an undirected graph throughout the course of the quarter. And undirected graphs have edges that have no orientation, OK? So if I'm trying to get from city A to city B, I'm going to have a edge that connects the two. If it's undirected, that means I can get from city A to city B or from city B back to city A. So I'm just going to put one edge in my graph and say, it's an undirected graph. Usually, it's just drawn with a straight line and that's representing that you can go either direction, OK?

You also have some graphs that are what we call directional graphs. So directional graphs, they still have the same thing. The edges are going to say, city A city B, but it's important to understand that if you say city A city B, that it means from city A to city B, and not the other way around. Maybe it's a one-way road that goes that direction, or maybe going from city A to city B is full of traffic, but city B back to city a is not traffic-y at all because it's a reverse commute.

And so you might actually have to have two directed edges, one going one way, one going the other way, with possibly different costs associated with them. So there is a lot of graphs that we might have directed edges on them. And often, we see those written with little arrows that show up. And so one of the things that we'll always end up talking about whenever I talk about a graph, I'll probably indicate either through the picture or through talking about it, is this an undirected graph or is this a directed graph? Because that's an important distinction to make between the two.

We often get loops. If you can go from a vertex to itself, you get a loop. It's going to turn out that that's not going to be very important for most of the things that we do because we don't have a lot of those style loops in the algorithm things we're going to be looking at. In mathematics, you might have a lot more of those.

Two edges with the same end vertices are considered parallel. So I might have an edge that goes from city A to city B, and I might have another edge that goes from city A to city B, OK? And you might wonder why you have both of those? Well, possibly in an airline-type simulation, you might have two distinct airlines that fly from, say, Denver to Los Angeles. And I want to possibly have two lines that do the Denver to Los Angeles edge of representing the two different airlines because possibly they have different costs of the airline in terms of doing that, and they have to mark those things specifically.

So you might have a need for doing some of that, depending on what you're modeling. And then a simple graph is one that has no loops or parallel edges, OK? These are the types of graphs we're going to be spending probably a lot of time working on. No little crazy loops, no parallel edges. Almost all the graphs we're going to be looking at are going to be these sort of basic, simple graphs.

So a few more definitions right here. We're not going to use the term head and tail all that much. Sometimes these are referred to head and tail. Sometimes you see them referred to as source and destination. I know in some of the parallel graph languages like Spark, for example, we've refer to them as source and destination. It's basically, in a directed graph, where you're coming from, where you're going to, OK? So those are terms that you might need to know.

These are definite terms that we're going to take a look at right here. If you have an edge that connects vertices u and v, for example, we're going to say vertices u and v are adjacent to each other, OK? Doesn't mean they're standing up right next to each other. It just means they have an edge that connects them. So we'll use the term adjacent vertices all the time in this course, and that's what we mean.

And you can reverse that if you want, and you can say, the edge is incident with both those two vertices, as well. And so you can talk about incident edges if you want as well. Just another term that we can use to talk about sort of the adjacency of things and how they're related. This whole section on degrees is important for certain types of algorithms when we're going through. And the degree on a graph is basically talking about how many edges that you have at particular vertices.

So what we're talking about is we have to look at a particular vertex, and we basically look at how many edges are connected to it. If I'm a vertex and I can connect to three different other vertices with three different edges, then my degree is 3, OK? As soon as you have a directional graph, you can not only talk about the degree, but you can also talk about the in degree and the out degree. How many edges do I have going out to other people, and how many just do I have coming in the other way from other people? And sometimes those in degree, out degree, and just standard degrees are important, depending on the type of algorithm that we're looking at.

We're also going to spend a lot of time, especially later in the quarter, talking about weighted graphs, OK? So weighted graphs have this extra little piece right here. We've got vertices, edges, and weights. And basically, sometimes these weights are sort of included in the edge, but the idea is we don't just have a connection between all the vertices, but the connection itself-- the edge itself-- has a cost associated with it.

A distance, for example, on a map. city A is connected to city B by a road, and the road is 235 kilometers long. And so that would be the weight that's associated. We do a lot of that when we're doing the algorithm stuff. So what else do we have?

So some simple little graphs just to sort of show you what the pictures look like right here. We've got a simple, undirected graph G-- And we often refer to graphs as G, or G1, or G2-- consists of a non-empty set of vertices and a set of edges, OK? And so, basically, these are the types of graphs we're going to be using. And there's other things that we can talk about with this, but this is probably the most important one for us right here.

We're going to see these pictures of graphs all the time. So I have vertices a, b, c, d, e, f, and g. I have edges between a and b, a and c, b and c, and edges here and here, and I have an edge here. And so we'll list our vertices out as a little set, and you'll see the edges listed out as a set of pairs like this, where they're talking about all the vertices they're connected together with. So you very often see them mathematically listed like this.

There's other ways you can actually see the graph defined, and we'll talk about this soon enough, but this is a very mathematical definition for what a graph is. So sometimes you just see the picture, sometimes you see this mathematical definition, and those represent our graphs.

So just some common types of graphs. So one of the things that we will mentioned a few times going through the course is that we might have a complete graph. These are usually good from a theoretical standpoint, but a complete graph is a graph where every note is connected to every other node. So got a couple examples. They don't really get interesting until right here and right here, but here, I have every node connected to every other node.

So this would be like having your nodes be cities and having roads that connect everything to everything else. And so these are often useful from a theoretical standpoint. Because when we're dealing with algorithms and dealing with efficiency, often, the worst efficiency that we get happens to be on situations where our model happens to be fully connected or almost fully connected, and we have lots of choices of where to go, right?

If we have some sort of routing algorithm and we don't have a whole lot of roads to choose from, it's not going to be that intensive because it's going to be easier to choose our roads. But if we have a fully connected map with lots of roads going everywhere, that's going to balloon really fast, in terms of efficiency, in terms of time it takes to run because we just have so many edges. So we often use these as examples for nice cases to test, does our algorithm scale up? Can we do an example that has lots of these edges?

We often talk about paths. So paths are simply, if I want to get from this vertex to this vertex right here, I'm going to follow some path through a bunch of other vertices. And there might be a whole bunch of other vertices in here that are connected to this that I'm just not showing on this particular graph, but a path is a sequence of edges that go through a bunch of vertices to get to my destination. And very often, we're trying to find maybe a least cost path through a graph. So that's what a path is.

Cycles. Cycles are often things that cause issues for our algorithms, but cycles are when we have a vertex, and we end up back at that same vertex in some way, right? I'm going along and I'm following a path, and I end up looping back around. And cycles are always hard because, when you loop back around, you can often end up repeating things again and again and get yourself stuck.

And that's not the sort of thing that we want to do, so what we often end up needing to do is we either need to make sure that our models don't have cycles in them when we build the models. Or if we notice that, because the way our data is set up, we actually have cycles built into our model, then that means when we start to code it, we need to be cognizant of, do we need to do something special about the cycles and notice if I'm circling back around and maybe not do that sort of thing. So noticing if there's cycles can be pretty important.

We have a couple of different graph types here that we may be working with. So bipartite graphs are graphs like these two. It's probably easier to take a look at this first than it is to read the definition, but the idea would be you can actually partition your set of vertices into a couple different sets. So I'm going to partition my thing into two sets, a set of vertices U and a set of vertices V, such that every edge is incident across.

So in other words, the red nodes right here, they all connect to the black nodes, and the black nodes all connect to the red nodes, but the red nodes don't connect to each other, and the black nodes don't connect to each other. And so that sort of graph can be useful to notice if you have that type of graph and there are types of algorithms where we're trying to solve those sort of equations.

Those are sort of mathematical representations. And clearly, there's other graph types and other more rigorous mathematical things we could put in there, but I tried to highlight some of the ones that we're going to be using so don't need to keep reintroducing those terms. But I also want to mention a couple of things specifically with computer representation, OK? So this is less mathematical and more, how are we going to possibly represent our graphs in the computer? Because we're going to be using a lot of these graph data structures.

So these two pictures right here are actually the exact same graph, OK? They both have five vertices. They both have nodes that are connected to each other. This guy is connected to here, this guy's connected to here, and these guys are connected to this way. I have the same thing. This node is connected to here, which is connected to here, which is connected to here, which is connected to here.

And so I would just have to-- let me just draw on this right here. I would just have to relabel these because I haven't actually labeled these things. So if I label this A, and B, and C, and D, and E, and if I label these guys A and B, and C, and D, and E, I can actually end up with the exact same graph. And so the picture of the graph is not as important as what nodes are in it-- what vertices are in it-- and then the edges that connect those two. So we can draw it in lots of different ways. And those don't look like they're the same graph, but they could be the same graph if that's the way the edges happen to be labeled.

So that's what I mean by a graph is not a picture, it's a set of vertices and a set of edges. And this is often how we would do this and. We listed the set of vertices right here and the set of edges. And this was matching very similarly to that mathematical definition that I just gave. And so when we actually put this into programs later on-- because we are building these models, and we're talking about modeling right here. But eventually, we're going to have to encode this model into a program like Python, so we're going to need to know how to represent this.

There's a couple of different ways we can do it. There's a adjacency matrices and adjacency lists. So adjacency matrix is very often one of the more efficient ways of doing it. It tends not to be the mathematical model everybody thinks of first. So this is what my adjacency matrix would look like. I'm just going to skip the mathematical definition at the start and go straight to the picture, and then we can go back and talk about the mathematical definition.

If this is my graph right here, I have these six vertices and all of these edges. And so my adjacency matrix is going to be a 2 by 2-- not a 2 by 2, a two-dimensional-- sorry, a 6 by 6 matrix-- hence, adjacency matrix-- of connectivity information. And so the idea is what we're going to go through here. And we're going to put a 1 if two nodes are connected and a 0 if they're not connected.

So node 1 is connected to node 2. And so this is going to be the row for node 1. And I'm just going to draw on this here. Let me switch to my pen. So this is the row for node 1, and this is the connections to 1 2, 3, 4, 5, and 6. So node 1 is connected to node 2. Node 1 is also connected to node 3, and it's connected to node 4, but it's not connected to itself, and it's not connected to node 5 and 6.

And so you have one of these rows for 2 and one of these rows for 3. You have a row for all the connectivity. And so this is basically just a little matrix that tells you how everything is connected with everything else. This does take up a little bit of space, but it makes lookup very efficient. If I want to know if two vertices are connected, if I want to know if vertex 2 is connected to vertex 5, I literally just go to 2, zip over here to 5, and just look up that value right there. And I can say, yes, 2 is connected to 5. So it takes a little bit of space to store, but it tends to be very efficient for lookup.

With that said, the other way to do it is sort of more of the mathematical definition or closer to the mathematical definition, where you have lists of adjacencies. And so with these lists of adjacencies, again, we have the same graph here, and I can represented a completely different way over here. And the idea is that I'm just going to list what I'm adjacent to. So 1 is adjacent to 2, 3, and 4, but not to 5 and 6. So you get a list of things.

And there's actually another way you can represent it as well. I'll just back up two slides. This is the other way that you can represent it right here. You can actually just give all the pairs. 1 is related to 2, 2 is related to 3. I could have written out all the pairs, and sometimes you see that as well. But with an adjacency list, for example, compared to the adjacency matrix, this actually takes up less space-- perhaps less space-- but it's definitely harder to find, right?

If I want to find, is 3 connected to node 5, OK? Well, I can just jump to node 3's list right here. But then to find if it's connected to node 5, I've got to go, well, where is it in the list? Is this 5? Is this 5? Is this 5? Is this 5? And I've got to sort of search down the list to try to find the one I want. And so finding if nodes are adjacent is it going to be a little bit more cumbersome in terms of speed than it would have been with an adjacency matrix.

But the one thing that I might gain out of this is that if my adjacency matrix-- let me go back to this for just a second-- if my adjacency matrix is pretty sparse-- and what do I mean by that? I have a graph that isn't very connected. There's going to be a lot of 0s on here, OK? So I built this big table that has a lot of 0s, and those 0s aren't really giving us any information. They're just wasting space. What I'm concerned about is the 1s.

And so if I have a graph that doesn't have a lot of edges, I'm building this big table that has very little 1s, and I'm wasting a lot of space, where the adjacency list-- these lists, then, would be really small because you don't have much connected. And so it's going to take a lot less space. And actually, with a really small list, it's pretty efficient to look stuff up in it.

So, which one is more efficient for you sometimes depends on are you trying to save some space, are you trying to get speed, which one do you care more about, and how connected is your graph, actually? If it's super connected, then adjacency matrices probably make more sense.

And then lastly, we have here-- I have some path and connectedness stuff. And so one of the things here is we often will draw our graphs like this. And so we've got our graph right here connected with vertices and edges, and this is going to be a undirected graph. And so, as I said, with undirected graphs, we actually usually draw them like this without arrows between here.

And what we're looking for is, is there a path of, say, length k from one node to the other, OK? And that's a question we're going to ask all the time. And one of the things that I haven't really talked about right here is distances between things. That's one of the things we're concerned about. So there is a path from node 1 to, say, node 6. And what's the distance?

Well, do you go here, here, here, or do you go here, here, here here, here? And so the distance between those two could vary. We might want to talk about shortest distance. There's all sorts of things we could talk about when we start actually implementing our algorithms with this graph. We could talk about graphs that are connected together.

Clearly, every note is connected to every other node in this graph. If you have a graph with-- if I add some nodes right here, if I added a couple more nodes right here and here, and I connected these two together, those two would be connected together, but they wouldn't be connected to the other graphs.

And so you can do things like connected components, where you figure out that, hey, all these guys are connected together, all. These guys are not so we often ask questions about distance and connection information when we're doing graphs. And that's just what they mean when I talk about graphs, whether they're connected or whether there's a path from one thing to another.



## Graph Models

So in this lecture, we are going to be reviewing graph models.

Modeling is a very important first step in understanding how to write algorithms because we have to be able to model our data that we're getting in, and then we develop algorithms based off of that. So graph models tend to be a big one that we use throughout this course, and they tend to be things that, if you haven't done anything with graphs and a little bit, you tend to forget some of the terminology. So we're going to spend a little bit of time going over some of the background terminology and graphs so that, later on in the course, I can just refer to specifics on graphs without having to talk about it every time a graph comes up.

So we have looked at a couple of previous examples in a previous lecture. One of them was a sensor network, where we had a bunch of sensors that could sense up to a certain radius and talk to other sensors within a certain radius. And we wanted to figure out, hey, can they actually talk to each other, can they actually communicate with each other, or do I have to place one of my sensors in a different location for them to actually send information all the way across to fully track somebody?

And so one of the things that we could end up doing is we could implement this with graphs. And so if you actually take a look at my sensor networks right here, I might have this sensor right here that has this radius and this sensor network right here that has this other radius right here. And since these two radii overlap with each other, what I could do is I could build a graph. And I could make where the locations of my sensors are be these nodes of a graph, and I could make the edges across the connections be the edges.

So if these sensor networks overlap, they can talk to each other. This sensor network and this sensor network overlap, they can talk to each other. And so the idea would be you could build up a graph that sort of described the connectivity of your sensor networks. And then once this graph was built up, you wouldn't need to have all these concentric circles all over the place.

You could just have the locations and the connectivity. And that would allow you to talk about, is it a connected graph, or is it two pieces that aren't connected and I need to do something to connect it, or now that I know it's connected and I want to send information from one to the next, how do I do that? How do I communicate from this one down to this one? Who do I have to talk to? Because I can't send it directly to that sensor. I have to send it indirectly through other pieces.

So this graph idea, it's a pretty powerful idea. And we're doing that all the time, where we're taking the input we have, and we might build up some sort of graph that describes my network. Now, this one was fairly easy to put it into graph form because it's this physical arrangement, right? We have sensor networks physically at various spots, and you can think about that is a physical graph.

The other example that we did was the one with the Facebook data that I had introduced, where I wanted to know if friends are you know transitive, right? If I'm friends with Riley and Riley's friends with Nolan, am I friends with Nolan too, right? Now, that doesn't sound, at least on the surface, like it would be obvious, I want to do a graph with that. Because transitivity is kind of described mathematically. And you're not thinking graphs because you tend to think graphs when you think geometrically like you would with a sensor network.

But you can do this very easily with graphs. You can actually create nodes for each person. And they're not physically in these locations, but they're just nodes between them. And then what you would do is you could actually create links or edges between two people if they happen to be friends. So if I'm friends with Riley and Riley's friends with Nolan, am I friends with Nolan too? If this was me and this was Riley and Nolan, then the answer would be I am not, in that particular case.

And so you can use this graph idea to model all sorts of things. And I'm not saying that graphs are the only way to model any of these things. It's just a very common model. and it's a model that some people don't necessarily always think about, and it's a model that we're going to be using a lot in this class to do various things.

So now that we have sort of the idea that I can take my data and maybe put it into graph models as a modeling technique, let's spend some time talking about graph basics. And I'm sure, at some point, you learned all sorts of things about graphs. A lot of these concepts are probably familiar. But it may be last week you heard about them or it may be several years ago you heard about them, so we're going to go through and talk about a bunch of terms right here so that we can get familiar with graphs again so that we can use them more easily.

And again, I kind of mentioned this right here. We have more than just those two problems. All sorts of problems can be done, right? So mathematical things like relations can be done with graphs. I showed you an example of that with a friends. Biological structures can be done-- so an example of something like this. We often do think about graphs for things like those molecules and stuff like that.

World Wide Web stuff, right? The web is connected together in various ways, and so that can be modeled as a graph. Subway and road maps, OK? We're used to kind of looking at a picture of a map and not thinking about, oh, I've got locations like street corners and I've got roads that connect them, or I've got subway stops and train things that connect them. We tend to think more about them for subways and mass transit because we tend to see the map drawn out as a graph a lot, but you tend not to think about it as much for road maps.

But that's exactly what they're modeling it as when they're doing things on all those mapping applications you have on your phone, is they're turning that pretty map you're seeing into a graph behind the scenes and doing all their algorithmic computation on that graph. Social networks, we talked about that a little bit. Polygonal meshes. So things like this little dolphin right here, this is a graphic thing. It's really just a graph as well, in terms of doing stuff. But just tons and tons of things that we can end up turning into graphs.

So onto the definitions here. So a graph has two pieces, OK? It's got vertices, and it's got edges. Sometimes I'm going to call the vertices nodes, but I'll kind of go back and forth with that. But we almost always mathematically call them vertices. And whenever you see the term v when you're talking about graphs, v is referring to the vertices, OK? And oftentimes, with the mathematical notation, when you see a capital V, it tends to mean a set of vertices. When you see a capital E, it tends to mean a set of edges that connect those two vertices together.

You see definitions like this all the time. E is a finite multiset of pairs from V cross V. What does that mean? It means, basically, it's a pair of vertices, right? I'm going to go from vertex A to vertex B, so the edge is going to be something that represents vertex A to vertex B, OK? And so that's just how you read some of that mathematical notation, and we need both vertices and edges to actually form our graph.

We talk a lot about an undirected graph throughout the course of the quarter. And undirected graphs have edges that have no orientation, OK? So if I'm trying to get from city A to city B, I'm going to have a edge that connects the two. If it's undirected, that means I can get from city A to city B or from city B back to city A. So I'm just going to put one edge in my graph and say, it's an undirected graph. Usually, it's just drawn with a straight line and that's representing that you can go either direction, OK?

You also have some graphs that are what we call directional graphs. So directional graphs, they still have the same thing. The edges are going to say, city A city B, but it's important to understand that if you say city A city B, that it means from city A to city B, and not the other way around. Maybe it's a one-way road that goes that direction, or maybe going from city A to city B is full of traffic, but city B back to city a is not traffic-y at all because it's a reverse commute.

And so you might actually have to have two directed edges, one going one way, one going the other way, with possibly different costs associated with them. So there is a lot of graphs that we might have directed edges on them. And often, we see those written with little arrows that show up. And so one of the things that we'll always end up talking about whenever I talk about a graph, I'll probably indicate either through the picture or through talking about it, is this an undirected graph or is this a directed graph? Because that's an important distinction to make between the two.

We often get loops. If you can go from a vertex to itself, you get a loop. It's going to turn out that that's not going to be very important for most of the things that we do because we don't have a lot of those style loops in the algorithm things we're going to be looking at. In mathematics, you might have a lot more of those.

Two edges with the same end vertices are considered parallel. So I might have an edge that goes from city A to city B, and I might have another edge that goes from city A to city B, OK? And you might wonder why you have both of those? Well, possibly in an airline-type simulation, you might have two distinct airlines that fly from, say, Denver to Los Angeles. And I want to possibly have two lines that do the Denver to Los Angeles edge of representing the two different airlines because possibly they have different costs of the airline in terms of doing that, and they have to mark those things specifically.

So you might have a need for doing some of that, depending on what you're modeling. And then a simple graph is one that has no loops or parallel edges, OK? These are the types of graphs we're going to be spending probably a lot of time working on. No little crazy loops, no parallel edges. Almost all the graphs we're going to be looking at are going to be these sort of basic, simple graphs.

So a few more definitions right here. We're not going to use the term head and tail all that much. Sometimes these are referred to head and tail. Sometimes you see them referred to as source and destination. I know in some of the parallel graph languages like Spark, for example, we've refer to them as source and destination. It's basically, in a directed graph, where you're coming from, where you're going to, OK? So those are terms that you might need to know.

These are definite terms that we're going to take a look at right here. If you have an edge that connects vertices u and v, for example, we're going to say vertices u and v are adjacent to each other, OK? Doesn't mean they're standing up right next to each other. It just means they have an edge that connects them. So we'll use the term adjacent vertices all the time in this course, and that's what we mean.

And you can reverse that if you want, and you can say, the edge is incident with both those two vertices, as well. And so you can talk about incident edges if you want as well. Just another term that we can use to talk about sort of the adjacency of things and how they're related. This whole section on degrees is important for certain types of algorithms when we're going through. And the degree on a graph is basically talking about how many edges that you have at particular vertices.

So what we're talking about is we have to look at a particular vertex, and we basically look at how many edges are connected to it. If I'm a vertex and I can connect to three different other vertices with three different edges, then my degree is 3, OK? As soon as you have a directional graph, you can not only talk about the degree, but you can also talk about the in degree and the out degree. How many edges do I have going out to other people, and how many just do I have coming in the other way from other people? And sometimes those in degree, out degree, and just standard degrees are important, depending on the type of algorithm that we're looking at.

We're also going to spend a lot of time, especially later in the quarter, talking about weighted graphs, OK? So weighted graphs have this extra little piece right here. We've got vertices, edges, and weights. And basically, sometimes these weights are sort of included in the edge, but the idea is we don't just have a connection between all the vertices, but the connection itself-- the edge itself-- has a cost associated with it.

A distance, for example, on a map. city A is connected to city B by a road, and the road is 235 kilometers long. And so that would be the weight that's associated. We do a lot of that when we're doing the algorithm stuff. So what else do we have?

So some simple little graphs just to sort of show you what the pictures look like right here. We've got a simple, undirected graph G-- And we often refer to graphs as G, or G1, or G2-- consists of a non-empty set of vertices and a set of edges, OK? And so, basically, these are the types of graphs we're going to be using. And there's other things that we can talk about with this, but this is probably the most important one for us right here.

We're going to see these pictures of graphs all the time. So I have vertices a, b, c, d, e, f, and g. I have edges between a and b, a and c, b and c, and edges here and here, and I have an edge here. And so we'll list our vertices out as a little set, and you'll see the edges listed out as a set of pairs like this, where they're talking about all the vertices they're connected together with. So you very often see them mathematically listed like this.

There's other ways you can actually see the graph defined, and we'll talk about this soon enough, but this is a very mathematical definition for what a graph is. So sometimes you just see the picture, sometimes you see this mathematical definition, and those represent our graphs.

So just some common types of graphs. So one of the things that we will mentioned a few times going through the course is that we might have a complete graph. These are usually good from a theoretical standpoint, but a complete graph is a graph where every note is connected to every other node. So got a couple examples. They don't really get interesting until right here and right here, but here, I have every node connected to every other node.

So this would be like having your nodes be cities and having roads that connect everything to everything else. And so these are often useful from a theoretical standpoint. Because when we're dealing with algorithms and dealing with efficiency, often, the worst efficiency that we get happens to be on situations where our model happens to be fully connected or almost fully connected, and we have lots of choices of where to go, right?

If we have some sort of routing algorithm and we don't have a whole lot of roads to choose from, it's not going to be that intensive because it's going to be easier to choose our roads. But if we have a fully connected map with lots of roads going everywhere, that's going to balloon really fast, in terms of efficiency, in terms of time it takes to run because we just have so many edges. So we often use these as examples for nice cases to test, does our algorithm scale up? Can we do an example that has lots of these edges?

We often talk about paths. So paths are simply, if I want to get from this vertex to this vertex right here, I'm going to follow some path through a bunch of other vertices. And there might be a whole bunch of other vertices in here that are connected to this that I'm just not showing on this particular graph, but a path is a sequence of edges that go through a bunch of vertices to get to my destination. And very often, we're trying to find maybe a least cost path through a graph. So that's what a path is.

Cycles. Cycles are often things that cause issues for our algorithms, but cycles are when we have a vertex, and we end up back at that same vertex in some way, right? I'm going along and I'm following a path, and I end up looping back around. And cycles are always hard because, when you loop back around, you can often end up repeating things again and again and get yourself stuck.

And that's not the sort of thing that we want to do, so what we often end up needing to do is we either need to make sure that our models don't have cycles in them when we build the models. Or if we notice that, because the way our data is set up, we actually have cycles built into our model, then that means when we start to code it, we need to be cognizant of, do we need to do something special about the cycles and notice if I'm circling back around and maybe not do that sort of thing. So noticing if there's cycles can be pretty important.

We have a couple of different graph types here that we may be working with. So bipartite graphs are graphs like these two. It's probably easier to take a look at this first than it is to read the definition, but the idea would be you can actually partition your set of vertices into a couple different sets. So I'm going to partition my thing into two sets, a set of vertices U and a set of vertices V, such that every edge is incident across.

So in other words, the red nodes right here, they all connect to the black nodes, and the black nodes all connect to the red nodes, but the red nodes don't connect to each other, and the black nodes don't connect to each other. And so that sort of graph can be useful to notice if you have that type of graph and there are types of algorithms where we're trying to solve those sort of equations.

Those are sort of mathematical representations. And clearly, there's other graph types and other more rigorous mathematical things we could put in there, but I tried to highlight some of the ones that we're going to be using so don't need to keep reintroducing those terms. But I also want to mention a couple of things specifically with computer representation, OK? So this is less mathematical and more, how are we going to possibly represent our graphs in the computer? Because we're going to be using a lot of these graph data structures.

So these two pictures right here are actually the exact same graph, OK? They both have five vertices. They both have nodes that are connected to each other. This guy is connected to here, this guy's connected to here, and these guys are connected to this way. I have the same thing. This node is connected to here, which is connected to here, which is connected to here, which is connected to here.

And so I would just have to-- let me just draw on this right here. I would just have to relabel these because I haven't actually labeled these things. So if I label this A, and B, and C, and D, and E, and if I label these guys A and B, and C, and D, and E, I can actually end up with the exact same graph. And so the picture of the graph is not as important as what nodes are in it-- what vertices are in it-- and then the edges that connect those two. So we can draw it in lots of different ways. And those don't look like they're the same graph, but they could be the same graph if that's the way the edges happen to be labeled.

So that's what I mean by a graph is not a picture, it's a set of vertices and a set of edges. And this is often how we would do this and. We listed the set of vertices right here and the set of edges. And this was matching very similarly to that mathematical definition that I just gave. And so when we actually put this into programs later on-- because we are building these models, and we're talking about modeling right here. But eventually, we're going to have to encode this model into a program like Python, so we're going to need to know how to represent this.

There's a couple of different ways we can do it. There's a adjacency matrices and adjacency lists. So adjacency matrix is very often one of the more efficient ways of doing it. It tends not to be the mathematical model everybody thinks of first. So this is what my adjacency matrix would look like. I'm just going to skip the mathematical definition at the start and go straight to the picture, and then we can go back and talk about the mathematical definition.

If this is my graph right here, I have these six vertices and all of these edges. And so my adjacency matrix is going to be a 2 by 2-- not a 2 by 2, a two-dimensional-- sorry, a 6 by 6 matrix-- hence, adjacency matrix-- of connectivity information. And so the idea is what we're going to go through here. And we're going to put a 1 if two nodes are connected and a 0 if they're not connected.

So node 1 is connected to node 2. And so this is going to be the row for node 1. And I'm just going to draw on this here. Let me switch to my pen. So this is the row for node 1, and this is the connections to 1 2, 3, 4, 5, and 6. So node 1 is connected to node 2. Node 1 is also connected to node 3, and it's connected to node 4, but it's not connected to itself, and it's not connected to node 5 and 6.

And so you have one of these rows for 2 and one of these rows for 3. You have a row for all the connectivity. And so this is basically just a little matrix that tells you how everything is connected with everything else. This does take up a little bit of space, but it makes lookup very efficient. If I want to know if two vertices are connected, if I want to know if vertex 2 is connected to vertex 5, I literally just go to 2, zip over here to 5, and just look up that value right there. And I can say, yes, 2 is connected to 5. So it takes a little bit of space to store, but it tends to be very efficient for lookup.

With that said, the other way to do it is sort of more of the mathematical definition or closer to the mathematical definition, where you have lists of adjacencies. And so with these lists of adjacencies, again, we have the same graph here, and I can represented a completely different way over here. And the idea is that I'm just going to list what I'm adjacent to. So 1 is adjacent to 2, 3, and 4, but not to 5 and 6. So you get a list of things.

And there's actually another way you can represent it as well. I'll just back up two slides. This is the other way that you can represent it right here. You can actually just give all the pairs. 1 is related to 2, 2 is related to 3. I could have written out all the pairs, and sometimes you see that as well. But with an adjacency list, for example, compared to the adjacency matrix, this actually takes up less space-- perhaps less space-- but it's definitely harder to find, right?

If I want to find, is 3 connected to node 5, OK? Well, I can just jump to node 3's list right here. But then to find if it's connected to node 5, I've got to go, well, where is it in the list? Is this 5? Is this 5? Is this 5? Is this 5? And I've got to sort of search down the list to try to find the one I want. And so finding if nodes are adjacent is it going to be a little bit more cumbersome in terms of speed than it would have been with an adjacency matrix.

But the one thing that I might gain out of this is that if my adjacency matrix-- let me go back to this for just a second-- if my adjacency matrix is pretty sparse-- and what do I mean by that? I have a graph that isn't very connected. There's going to be a lot of 0s on here, OK? So I built this big table that has a lot of 0s, and those 0s aren't really giving us any information. They're just wasting space. What I'm concerned about is the 1s.

And so if I have a graph that doesn't have a lot of edges, I'm building this big table that has very little 1s, and I'm wasting a lot of space, where the adjacency list-- these lists, then, would be really small because you don't have much connected. And so it's going to take a lot less space. And actually, with a really small list, it's pretty efficient to look stuff up in it.

So, which one is more efficient for you sometimes depends on are you trying to save some space, are you trying to get speed, which one do you care more about, and how connected is your graph, actually? If it's super connected, then adjacency matrices probably make more sense.

And then lastly, we have here-- I have some path and connectedness stuff. And so one of the things here is we often will draw our graphs like this. And so we've got our graph right here connected with vertices and edges, and this is going to be a undirected graph. And so, as I said, with undirected graphs, we actually usually draw them like this without arrows between here.

And what we're looking for is, is there a path of, say, length k from one node to the other, OK? And that's a question we're going to ask all the time. And one of the things that I haven't really talked about right here is distances between things. That's one of the things we're concerned about. So there is a path from node 1 to, say, node 6. And what's the distance?

Well, do you go here, here, here, or do you go here, here, here here, here? And so the distance between those two could vary. We might want to talk about shortest distance. There's all sorts of things we could talk about when we start actually implementing our algorithms with this graph. We could talk about graphs that are connected together.

Clearly, every note is connected to every other node in this graph. If you have a graph with-- if I add some nodes right here, if I added a couple more nodes right here and here, and I connected these two together, those two would be connected together, but they wouldn't be connected to the other graphs.

And so you can do things like connected components, where you figure out that, hey, all these guys are connected together, all. These guys are not so we often ask questions about distance and connection information when we're doing graphs. And that's just what they mean when I talk about graphs, whether they're connected or whether there's a path from one thing to another.
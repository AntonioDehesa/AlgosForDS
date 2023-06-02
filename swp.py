# Imports
from collections import defaultdict

class MyVertex:
    def __init__(self, id: int, dist: int = 0):
        self.id = id
        self.next = None
        self.dist = dist

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, vertex, dist):
        if not self.head:
            self.head = MyVertex(vertex, dist)
            self.tail = self.head
        else:
            self.tail.next = MyVertex(vertex, dist)
            self.tail = self.tail.next
    
    def dequeue(self):
        if not self.head:
            raise ValueError("Impossible to dequeue elements from an empty queue")
        else:
            vid = self.head.id
            dist = self.head.dist
            self.head = self.head.next
                
            return vid,dist
    
    def empty(self):
        return self.head == None
        
    def __str__(self):
        myAns = "{"
        current = self.head
        while current:
            myAns+= str(current.id)
            myAns+= " : "
            myAns+= str(current.dist)
            if current.next:
                myAns+= ", "
            current = current.next
        myAns += "}"
        return myAns

def loadGraph(edgeFilename: str):
    my_vertices = defaultdict(set) # An empty set. We use a set because a person cant be friends with the same person twice
    try:
        with open(edgeFilename, "r") as myFile:
            for line in myFile:
                ids = line.split()
                my_vertices[int(ids[0])].add(int(ids[1]))
                my_vertices[int(ids[1])].add(int(ids[0]))
    except:
        print("No such file was found")
            
    return my_vertices

def BFS(G,s):
    dist= [-1 for i in range(len(G))] # We could set this to infinite, but setting it to -1 would accomplish the same
    queue = MyQueue() # We create the empty queue
    queue.enqueue(s,0) # We add the origin vertex to the queue
    dist[s] = 0 # The distance from the origin vertex to itself is 0
    while not queue.empty(): # loop till queue is empty
        curr,dis = queue.dequeue() # remove element from queue, saving which element it is, and the distance. 
        for edge in G[curr]: # loop for every neighbor
            if dist[edge] == -1: # If the distance has not been modified = not visited
                dist[edge] = dis + 1 # We add the distance of the current element plus one
                queue.enqueue(edge, dist[edge]) # We enqueue the current element
    return dist # finally return dist

def distanceDistribution(G):
    current_loop = 0
    distribution = defaultdict(int)
    for key in G.keys():
        distances = BFS(G,key)
        for i in distances:
            distribution[i]+=1
        current_loop+=1
        if current_loop == 1000:
            current_loop = 0
            print("====================")
            print("Current distributions:")
            s = sum(distribution.values())
            for k, v in distribution.items():
                if v > 0:
                    pct = v * 100.0 / s
                    print("[{}]: [{}]".format(k,pct))
            print("====================")
    s = sum(distribution.values())
    for k, v in distribution.items():
        if v > 0:
            pct = v * 100.0 / s
            distribution[k] = pct
    return distribution

#graph = loadGraph("edgesshort.txt")
graph = loadGraph("edges.txt")
distanceDistribution(graph)
res = distanceDistribution(graph)
for key, value in res.items():
    if value > 0:
        print("[{}]: [{}]".format(key,value))
# We could just print the entire dictionary, but most of them have a value of 0, so it would be unneccesary 
# The small world phenomenon indicates that most people in the world are just 6 people apart. 
# In this case, we see that morethan 90% of the vertex in the file are linked (know each other) through, at most, 6 other vertex. 
# So we can conclude that the phenomenon is true
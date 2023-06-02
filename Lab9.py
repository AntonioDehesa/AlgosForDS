# Dijkstra's shortest path greedy algorithm
# Find the min priority vertex from the list of given vertices
# Each vertex in the form of a list with priority as the first # element returns the min vertex and removes it from the list 
def extractMin(verts):
    minIndex = 0
    for v in range(1,len(verts)):
        if verts[v][1] < verts[minIndex][1]: 
            minIndex = v
    return verts.pop(minIndex)


# Dijkstra's shortest path algorithm 
def shortest(g):
    # Create a list of vertices and their current shortest distances
    # from vertex 0
    # [vertNum, dist] 
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]
    # Start at vertex 0 - it has a current shortest distance of 0 
    vertsToProcess[0][1] = 0
    # Start with an empty list of processed edges 
    vertsProcessed = []
    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess) 
        vertsProcessed.append(u)
        #print("to process:",vertsToProcess)
        #print(" processed:",vertsProcessed)
        # Examine all potential verts remaining 
        for v in vertsToProcess:
            # Only care about the ones that are adjacent to u 
            if g[u[0]][v[0]] > 0:
                # Update the distances if necessary 
                if u[1] + g[u[0]][v[0]] < v[1]:
                    v[1] = u[1] + g[u[0]][v[0]]
    print(vertsProcessed)

# # Prim´s MST algorithm 
# def mst(g):
#     nVerts = len(g)
#     keys = {}
#     P = {}
#     q = g.copy()
#     for i in range(nVerts):
#         keys[i] = float("inf")
#         P[i] = None
#     # We will use the same starting V as in shortest
#     keys[0] = 0
#     P[0] = -1
#     while q:
#         u = extractMin(q)
#         # Now we need to find the Vs that are adjacent to the node u
#         adjacents = [u.index(x) for x in u if x > 0] # Only those Vs that have a distance>0 are adjacent to the node
#         # Now we need to actually get those nodes from g
#         #resAdjacents = defaultdict(int)
#         #for v in adjacents:
#         #    resAdjacents[v] = g[v]

#         # Now that we actually have the adjacent nodes we can continue
#         for v in adjacents:
#             isVinQ = g[v] in q#resAdjacents[v] in q#g#q
#             uv = u[v]
#             z = keys[v]
#             x = g.index(u)
#             if isVinQ and uv < z:
#                 keys[v] = u[v]
#                 P[v] = x#g.index(u)
#     return P  

def mst(g):
    # We create the queue for the V and E
    Q = [[i, float("inf"), None] for i in range(len(g))]
    
    # Start at vertex 0 - it has a minimum edge weight of 0 to itself
    Q[0][1] = 0
    # List of processed edges
    P = []
    
    while Q:
        u = extractMin(Q)
        P.append(u)
        
        for v in Q:
            if g[u[0]][v[0]] > 0 and v[1] > g[u[0]][v[0]]:
                # Update the weight for v[1]
                v[1] = g[u[0]][v[0]]
                # And update v[2]
                v[2] = u[0]
    # Now we just build the answer
    mstEdges = [[v[0], v[2]] for v in P if v[2] is not None]
    # We add the reference to the root node, 0, which is -1. 
    mstEdges.insert(0, [P[0][0], -1])
    
    return mstEdges
# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
# The vertices didn't have labels in the videos
# so I'm using the following vertex labels:
# 2
# / \
# 3---1--7
# |\ |
# 4 | 0--6
# \|/
# 5
graph = [[0, 7, 0, 0, 0, 10, 15, 0],
[7, 0, 12, 5, 0, 0, 0, 9],
[0, 12, 0, 6, 0, 0, 0, 0],
[0, 5, 6, 0, 14, 8, 0, 0],
[0, 0, 0, 14, 0, 3, 0, 0],
[10, 0, 0, 8, 3, 0, 0, 0],
[15, 0, 0, 0, 0, 0, 0, 0],
[0, 9, 0, 0, 0, 0, 0, 0]]
#x=shortest(graph)
x=mst(graph)
print(x)


# There is one answer that is commented, and one that is running. 
# The commented one was my first attempt. I basically tried to use the algorithm in the slides directly, but it failed. Some nodes in P were never visited so they did not get updated.
# It looks weird with extra comments and variables, because I was still trying to make it work, but then I tried the second way, so I just commented it in case the other one did not work.
# Then, the one that is running is a combination of the algorithm in the slides, what I did, and the provided code, which actually worked. 
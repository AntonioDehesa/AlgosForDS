# Imports
from collections import defaultdict
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

# Prim´s MST algorithm 
def mst(g):
    nVerts = len(g)
    keys = []
    P = []
    for i in range(nVerts):
        keys.append([i, float("inf")])
        P.append([i, None])
    # We will use the same starting V as in shortest
    keys[0][1] = 0
    q = g.copy()
    while q:
        u = extractMin(q)
        # Now we need to find the Vs that are adjacent to the node u
        index = g.index(u)
        adjacents = [u.index(x) for x in u if x > 0] # Only those Vs that have a distance>0 are adjacent to the node
        # Now we need to actually get those nodes from g
        resAdjacents = defaultdict(int)
        for v in adjacents:
            resAdjacents[v] = (g[v])

        # Now that we actually have the adjacent nodes we can continue
        for v in adjacents:
            isVinQ = resAdjacents[v] in q
            isVinQ = v in q
            uv = u[v]
            z = keys[index][v]
            if isVinQ and uv < z:
                keys[index][v] = u[v]
                P[index][v] = u
            pass
    return P        

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
#shortest(graph)
x=mst(graph)
print(x)
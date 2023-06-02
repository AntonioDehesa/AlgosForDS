def printMatrix(m):
    for row in m:
        print(row)

def parenStr(parentLoc: list, matrixes: list = []):
    n = len(matrixes)
    if n == 1:
        return "({})".format(matrixes[0])
    else:
        i = int(matrixes[0][1])
        j = int(matrixes[n-1][1])
        location = matrixes.index("A{}".format(parentLoc[i][j])) + 1
        p1 = matrixes[0:location]
        p2 = matrixes[location:]
        resp1 = parenStr(parentLoc, matrixes=p1)
        resp2 = parenStr(parentLoc, matrixes=p2)
        res = "({}{})".format(resp1,resp2)
        return res

def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[float("inf") for i in range(n)] for j in range(n)]
    tracebackTable = [[None for i in range(n)] for j in range(n)]
    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0
    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1): 
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursive options
            for k in range(i,j):
                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1] 
                if q < m[i][j]:
                    m[i][j] = q
                    tracebackTable[i][j] = k
    Matrixes = ["A{}".format(i) for i in range(n)]
    bestParenthesis = parenStr(tracebackTable, matrixes=Matrixes)
    bestParenthesis = bestParenthesis[1:len(bestParenthesis)-1] # This line removes the final parenthesis, 
                                                                # which is not in the expected answer
    return bestParenthesis,m[0][n-1], m#tracebackTable

dims = [30,35,15,5,10,20,25]
#dims = [10,4,5,20,2]
bestParenthesis, minOps, tracebackTable = chainMatrix(dims)
print("Best Parenthesis location: \n{}".format(bestParenthesis))
print("Minimum operations: {}".format(minOps))
print("Traceback table: ")
for row in tracebackTable:
    print(row)
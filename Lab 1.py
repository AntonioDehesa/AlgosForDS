def printMatrix(m): 
    for row in m:
        print(row) 

def matrixMult(A,B):
    m = len(A) # Rows of A
    n = len(A[0]) # Columns of A
    p = len(B[0]) # Columns of B
    r = len(B) # Rows of B
    if n != r:
        print("""Unfortunately, the number of columns of matrix A and \n
              the number of rows of matrix B are not equal, so the matrix multiplication cannot be done.""")
        return None
    C = [[None for i in range(p)] for j in range(m)]
    for i in range(m):
        for j in range(p):
            C[i][j] = 0
            for k in range(r):
                x = A[i][k]
                y = B[k][j]
                C[i][j] += x*y
    return C

# Testing code
# Test1
A = [[ 2, -3, 3],
[-2, 6, 5],
[ 4, 7, 8]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)
# Test2
A = [[ 2, -3, 3, 0],
[-2, 6, 5, 1],
[ 4, 7, 8, 2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)
# Test3
A = [[ 2, -3, 3, 5],
[-2, 6, 5, -2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7],
[ 1, 2, 3]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)
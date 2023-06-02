# Finds ALL ways to place n nonattacking queens on a n x n board
# NOTE: State[i] is the row for the queen on Column i
# NOTE: There are solutions for n>3
# Stack ADT with list implementation from Lab 5
class MyStack(object):
    def __init__ (self, type): # Creates an empty list
        self.elemType = type 
        self.state = [] # Empty list
    def __str__ (self): # for print
        return str(self.state) 
    def empty(self):
        return len(self.state) == 0
    def push(self, elem): # Adds an element to the top of a stack 
        if type(elem) == self.elemType:
            self.state.append(elem)
        else:
            raise Exception("The element is not the same type as the eleemnts in the list")

    def pop(self): # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack") 
        else:
            return self.state.pop()
    def top(self): # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack") 
        else:
            return self.state[-1]

def nQueens(n):
    # Each state will include only the queens that have been placed so far
    initialState = [] # Initial empty state
    s = MyStack(list) # For a depth first search
    s.push(initialState) # Push the initial state onto the Stack
    # While we still have states to explore
    while not s.empty():
        currentState = s.pop() # Grab the next state
        currentCol = len(currentState)
        # See if we found a solved state at a leaf node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState) # Display the solution
        else:
        # Produce the state's children (if they are feasible)
        # Note children are produced backward so they come off the
        # stack later left to right
            for currentRow in range(n,0,-1):
            # Check horizontal and both diagonals of previous queens
                for previousCol in range(currentCol):
                    if (currentState[previousCol] == currentRow) or abs(currentState[previousCol]-currentRow) == (currentCol - previousCol):
                        break
                    else:
                    # Create child by making a copy and appending new col 
                        childState = currentState.copy() 
                        childState.append(currentRow)
                        s.push(childState) # Push child onto data structure
# Testing code (check 4,5,6,7)
# for n in range(4,15):
#    nQueens(n)

def graphColoring(graph, colors):
    n = len(graph)
    currentColors = []
    #initialState = [] # Initial empty state
    s = MyStack(list) # For a depth first search
    #s.push(initialState) # Push the initial state onto the Stack
    s.push([])
    # While we still have states to explore
    colors.reverse()
    while not s.empty():
        currentState = s.pop()
        if len(currentState) == 0:
            for color in colors: # We add every possible color node first, but we will visit them only if no other option
                temp = currentState.copy()
                temp.append(color)
                s.push(temp)
        else:
            availableColors = colors.copy()
            for i in range(len(currentState)):# We delete colors that have been used by adjacent nodes
                if graph[len(currentState)][i]: # If adjacent
                    try:
                        availableColors.remove(currentState[i])
                    except:
                        pass
            for color in availableColors:
                temp = currentState.copy()
                temp.append(color)
                s.push(temp)
        currentColors = s.top()              
        if len(currentColors) == n: # If every node has been colored successfully, then we dont need to continue looking
            break
    print(currentColors)
# Test data
# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
graph = [[False, True, False, False, False, True ], [True, False, True, False, False, True ], 
         [False, True, False, True, True, False], [False, False, True, False, True, False], 
         [False, False, True, True, False, True ], [True, True, False, False, True, False]]
colors = ['r', 'g', 'b'] 
graphColoring(graph, colors)
# expected answer
# ['r', 'g', 'r', 'b', 'g', 'b']
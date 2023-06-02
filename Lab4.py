def cPairDist(points: list[int]):
    points.sort() # First, we sort our list of points
    return recCPairDist(points)

def recCPairDist(points: list[int]):
    nPoints = len(points)
    if nPoints > 2:
        firstHalf, secondHalf = points[: int((nPoints)/2)], points[int((nPoints/2)):]
        lastInFirstHalf = firstHalf[-1]
        firstInSecondHalf = secondHalf[0]
        midDiff = abs(firstInSecondHalf - lastInFirstHalf)
        maxDiffFirstHalf = recCPairDist(firstHalf)
        maxDiffSecondHalf = recCPairDist(secondHalf)
        return max(maxDiffFirstHalf, maxDiffSecondHalf, midDiff)
    elif nPoints == 2:
        return abs(points[0] - points[1])
    else: 
        return points[0]

a = [7,4,12,14,2,10,16,6]
print("List A")
print(cPairDist(a))
b = [7, 4, 12, 14, 2, 10, 16, 5]
c = [14, 8, 2, 6, 3, 10, 12]
print("List B")
print(cPairDist(b))
print("List C")
print(cPairDist(c))
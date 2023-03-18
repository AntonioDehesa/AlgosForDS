# Imports
import random
import time

def merge(A,B):
    out = []
    i,j = 0,0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i+=1
        else:
            out.append(B[j])
            j+=1
    while i < len(A):
        out.append(A[i])
        i+=1
    while j < len(B):
        out.append(B[j])
        j+=1
    return out

def mergeSort(L: list[int]):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)
A = [i for i in range(100)]
random.shuffle(A)
print("Before sort")
print(A)
print("After sort")
print(mergeSort(A))

def insertionSort(L: list[int]):
    for i in range(1,len(L)):
        key = L[i]
        j = i-1
        while j>= 0 and L[j] > key:
            L[j+1] = L[j]
            j = j-1
        L[j+1] = key
    return L
A = [i for i in range(100)]
random.shuffle(A)
print("Before sort")
print(A)
print("After sort")
print(insertionSort(A))

def bubbleSort(L: list[int]):
    n = len(L)
    for i in range(n):
        for j in range(1,n-i):
            if L[j] < L[j-1]:
                L[j],L[j-1] = L[j-1],L[j]
    return L
A = [i for i in range(100)]
random.shuffle(A)
print("Before sort")
print(A)
print("After sort")
print(bubbleSort(A))

n = 100
print("N\t\tMerge\t\tInsert\t\tBubble")
while n <= 5000:
    A = [i for i in range(n)]
    random.shuffle(A)
    t1 = time.time()
    res = mergeSort(A)
    t2 = time.time()
    mtime = (t2-t1)*1000
    random.shuffle(A)
    t1 = time.time()
    res = insertionSort(A)
    t2 = time.time()
    itime = (t2-t1)*1000
    random.shuffle(A)
    t1 = time.time()
    res = bubbleSort(A)
    t2 = time.time()
    btime = (t2-t1)*1000
    print("{}\t\t{:.3f}\t\t{:.3f}\t\t{:.3f}".format(n,mtime,itime,btime))
    n+=100
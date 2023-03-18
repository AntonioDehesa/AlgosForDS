import random
n = 10
A = [i + 1 for i in range(n)]
random.shuffle(A)

print("Before sorting")
print(A)

for i in range(1,n):
    key = A[i]
    j = i-1
    while j>= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = key
print("After sorting:")
print(A)
from numpy import *

n = int(input("Enter N:"))
k = int(input("Enter K:"))
arr = zeros(n, dtype=int)
for i in range(len(arr)):
    arr[i] = int(input())
large = 0
for i in range(len(arr)):
    if arr[i] > large:
        large = arr[i]
if k<large:
    k=large-k
    print(k)
else:
    print("{:d}".format(0))


from itertools import product
a=list(map(int, input().split()))
b=list(map(int, input().split()))

t=tuple(product(a,b))
for items in t:
    print(items ,end=" ")

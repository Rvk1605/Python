# from itertools import permutations
# a,n=input().split()
# for i in range(int(n)):
#     p=list(permutations(a))
# print(p)



n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
i1=a.difference(b)
i2=b.difference(a)
u=i1.union(i2)
t=list(u)
t.sort()
for i in range(len(t)):
    print(t[i])
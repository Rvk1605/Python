n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
s=list(set(a))
for i in range(m):
    s.append(b[i])
    s.sort()
    s.reverse()
    r=s.index(b[i])
    print(r+1)





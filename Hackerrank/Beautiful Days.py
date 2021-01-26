r1,r2,k=input().split()
r1=int(r1)
r2=int(r2)
k=int(k)
count=0
def reverse(n):
    i = n
    rem = 0
    while i != 0:
        r = i % 10
        rem = rem * 10 + r
        i = i //10
    return rem
for i in range(r1,r2+1):
    day=(i-reverse(i))/k
    if day<0:
        day=-day
    if (day-int(day))==0:
        count=count+1
print(count)




n=int(input())
v=input()
flag=0
lst=[]
for i in range(len(v)):
    if v[i]=='U':
        flag=flag+1
    elif v[i]=='D':
        flag=flag-1
    lst.append(flag)
count=0
for i in range(len(lst)):
    if(lst[i]==-1 and lst[i-1]>=0):
        count=count+1
print(count)

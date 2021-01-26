s=input()
l=len(s)
s=list(s)
count=0
for i in range(l-1):
    if s[i]==s[i+1]:
        s[i]=0
        s[i+1]=0
for i in range(l):
    if(s[i]!=0):
        print(s[i],end='')
    else:
        count=count+1
if(count==l):
    print("Empty List")

s=input()
t=input()
k=int(input())
count=0
a=0
b=0
for i in range(len(s)):
    if s[i]==t[i]:
        pass
    else:
        a=len(s[i:len(s)])
        b=len(t[i:len(t)])
        break
if s is t:
    print("YES")
elif((a)+(b)<=k):
    print("YES")
else:
    print("NO")





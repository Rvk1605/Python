s=input()
# s=list(s)
# n=int(input())
# for i in range(n):
#     s.append(s[i])
#     if(len(s)==n):
#         break
# count=0
# for i in range(len(s)):
#     if(s[i]=='a'):
#         count=count+1
# print(count)
count=0
c=0
l=len(s)
for i in range(l):
    if s[i]=='a':
        count=count+1
n=int(input())
r=n//l
rem=n%l
print(rem)
for j in range(rem):
    if s[i]=='a':
        c=c+1

t=count*r
print(t+c)




# ch = input()
# length = len(ch)
# counter = 0
# co = 0
# for i in range(0,length):
#     if ch[i]=='a':
#         counter+=1
# glen = int(input())
# stri = int(glen//length)
# rem = int(glen%length)
# print(rem)
# for j in range(0,rem):
#     if ch[j]=='a':
#         co+=1
# print((stri*counter)+co)



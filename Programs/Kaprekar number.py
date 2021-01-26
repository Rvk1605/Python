# def check(n):
#     x=n*n
#     s=list(str(x))
#     length=len(s)
#     if length%2==0:
#         l=length/2
#         r=length-l
#     else:
#         l=length//2
#         r=length-l
#     s1=s[0:l]
#     s2=s[l:length]
#     s1=''.join(s1)
#     s2=''.join(s2)
#     if int(s1)+int(s2)==n:
#         return n
#
#
#
#
# r1 = int(input())
# r2 = int(input())
# l = []
# for i in range(r1,r2+1):
#     l.append(check(i))
# for j in l:
#     print(j,end='')

r1=int(input())
r2=int(input())
for i in range(r1,r2+1):
    x=i*i
    s=list(str(x))
    length=len(s)
    if length%2==0:
        l=length/2
        r=length-l
    else:
        l=length//2
        r=length-l
    s1=s[0:l]
    s2=s[l:length]
    s1=''.join(s1)
    s2=''.join(s2)
    print(s1,s2)
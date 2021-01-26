import math
# # def square_count(r1,r2):
# #     count=0
# #     for i in range(r1,r2+1):
# #         s=math.sqrt(i)
# #         if(s-int(s)==0):
# #             count=count+1
# #     return count
#
# n=int(input())
# c=[]
# for i in range(n):
#     r1,r2=map(int,input().split())
#     count = 0
#     for j in range(r1, r2 + 1):
#         if(math.sqrt(j).is_integer()):
#            count = count + 1
#     c.append(count)
# for k in c:
#     print(k)

#2nd Method By taking Squares
# n=int(input())
# c=[]
# for i in range(n):
#     r1,r2=input().split()
#     count = 0
#     for j in range(1,(int(r1)+int(r2)//3)):
#         if j*j >=int(r1) and j*j <=int(r2):
#             count=count+1
#     c.append(count)
# for k in c:
#     print(k)

def count(a,b):
    flag1=0
    flag2=0
    count=0
    for i in range(a, b):
        if math.sqrt(i).is_integer():
            x = math.sqrt(i)
            flag1=1
            break
    for j in range(b, a, -1):
        if math.sqrt(j).is_integer():
            y = math.sqrt(j)
            flag2=1
            break
    if flag1==1 and flag2==1:
        for k in range(int(x),int(y+1)):
            count=count+1
    return (count)
n=int(input())
res=[]
for i in range(n):
    x,y=map(int,input().split())
    r=count(x,y)
    res.append(r)
for j in res:
    print(j)

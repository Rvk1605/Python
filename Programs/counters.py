from collections import Counter
n=int(input("Enter no. of Shoes:"))
a=list(map(int, input().split()))
k=Counter(a).keys()
v=Counter(a).values()
customers=int(input("Enter no. of Customers:"))
lst=[]
for i in range(customers):
    lst=list(map(int,input().split()))




from numpy import*
x=int(input("Enter Rows:"))
y=int(input("Enter Columns:"))
a=zeros((x,y),dtype=int)
l=len(a)
print("Enter Array Elements")
for i in range(l):
    for j in range(len(a[i])):
        p=int(input())
        a[i][j]=p
#1st method to diaplay
print(a)
#2nd method
for i in range(l):
    for j in range(len(a[i])):
        print(a[i][j])

#3rd Method
for r in a:
    for k in r:
        print(k,end=" ")
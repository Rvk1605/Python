from numpy import*
n=int(input("Enter No. of Rows:"))
m=int(input("Enter No. of Columns:"))
a=zeros((n,m),dtype=int)
l=len(a)
print("Enter Elements:")
i=0

while i<l:
    j=0
    while j<len(a[i]):
        a[i][j]= list(map(int,input().split(" ")))

        j+=1
    i+=1
print(a)
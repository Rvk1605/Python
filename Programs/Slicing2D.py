from numpy import*
arr=ones((3,3),dtype=int)
l=len(arr)
for i in range(l):
    for j in range(len(arr[i])):
        x=int(input(""))
        arr[i][j]=x
print(arr)

#For Slicing
a=arr[1,0:2]
print(a)
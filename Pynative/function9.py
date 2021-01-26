def large():
    a=[]
    largest=0
    n=int(input("Enter No. of Elements:"))
    for i in range(n):
        x=int(input())
        a.append(x)
    for i in range(n):
        if(a[i]>largest):
            largest=a[i]
    return largest
l=large()
print("Largest = ",l)
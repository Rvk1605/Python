from array import*
natural=array('i',[])
n=int(input("Enter No. of Elements:"))
for i in range(n):
    natural.append(int(input()))
i=0

print("\n After Reversing")
natural.reverse()
while i<n:
    print(natural[i],end="\t")
    i+=1
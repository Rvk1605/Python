n=int(input("Enter a number:"))
i=n
count=0
while i!=0:
    r=i%10
    i=i//10
    count+=1
print(count)

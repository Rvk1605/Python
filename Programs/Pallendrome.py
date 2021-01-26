a=int(input("Enter the Number:"))
i=a
rem=0
while i!=0:
    r=i%10
    rem=rem*10+r
    i=i//10
print(rem)
if rem==a:
        print("Pallendrome")
else:
            print("Not Pallendrome")

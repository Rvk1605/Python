lst=["Raj","Rahul","Shuvam","Divi","Rakesh"]

#Print The Alternate Starting From Index = 0

print("Without Enumerator")

i=1
for item in lst:
    if(i%2!=0):
        print(f"{item}")
    i=i+1

print("\nWith Enumerator")

for index,item in enumerate(lst):
    if(index%2==0):
        print(f"{item}")
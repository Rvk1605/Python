n=int(input())
if(n>2 and n<6 and n%2==0):
    print("Not Wierd")
elif(n>5 and n<21 and n%2==0):
    print("Wierd")
elif(n>20 and n%2==0):    
    print("Not Wierd")
else:
        print("Wierd")
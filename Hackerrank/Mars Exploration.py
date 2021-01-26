m=input()
s="SOS"
no_message=len(m)//3
count=0
res=s*no_message
for i in range(len(m)):
    if res[i]==m[i]:
        pass
    else:
        count=count+1
print(count)

v=list(map(int, input().split()))
dict={'a':v[0],'b':v[1],'c':v[2],'d':v[3],'e':v[4],'f':v[5],'g':v[6],'h':v[7],'i':v[8],'j':v[9],'k':v[10],'l':v[11],'m':v[12],'n':v[13],'o':v[14],'p':v[15],'q':v[16],'r':v[17],'s':v[18],'t':v[19],'u':v[20],'v':v[21],'w':v[22],'x':v[23],'y':v[24],'z':v[25]}
s=input()
n=[]
for i in range(len(s)):
    n.append(dict[s[i]])
area=len(s)*max(n)
print(area)
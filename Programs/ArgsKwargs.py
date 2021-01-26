def fun(a,*b,**c):
    # print(a,"\n")
    # for item in b:
    #     print(item
    # print()
    # for key,value in c.items():
    #     print(f"{key} = {value}")
    # print()
    # for i in d:
    #     print(i)
    for i in range(len(b)):
        print(b[i])





a="My Name Is Rajveer"
b=["Raj","Chandu","Rahul"]
c={"Raj":"Doctor","Chandu":"IITIAN","Rahul":"Programmer"}
d=("Arayan","Shibom","Anish")
fun(a,*b,**c)
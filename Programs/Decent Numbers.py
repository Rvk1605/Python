    # A Decent Number has the following properties:
    #
    # Its digits can only be 3's and/or 5's.
    # The number of 3's it contains is divisible by 5.
    # The number of 5's it contains is divisible by 3.
    # It is the largest such number for its length.

    n=int(input())
    a=[]
    for i in range(n):
        x=int(input())
        a.append(x)
    for i in range(n):
        if a[i]<3:
            print("-1")
        elif a[i]%3==0:
            print("5"*a[i])
        elif a[i]%5==0:
            print("3"*a[i])
        elif a[i]>5 and a[i]%2!=0:
            if (a[i]-3)%5==0:
                print("5"*3+"3"*(a[i]-3))
            elif (a[i]-5)%3==0:
                print("5"*(a[i]-5)+"3"*5)
            else:
                t=a[i]//2
                f=(a[i]//2)+1
                print(("5"*f)+("3"*t))




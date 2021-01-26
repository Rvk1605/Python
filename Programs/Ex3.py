n=18
print("Your Have 9 Guess")
for i in range(9):
    a = int(input("Enter Your Guess:"))
    print("No of Guesses Left = ", 8 - i)
    if a>n and a<n+3 :
        print("You are Very Much Closer but more")
        continue
    elif a<n and a>n-3:
        print("You are Very Much Closer but less")
        continue
    elif(a>n+3):
        print("Your are Far Away Come Closer")
        continue
    elif(a<n-3):
        print("You are Far Behind Come Close")
        continue
    elif(a==n):
        print("           CONGRATULATIONS              ")
        print("***********You Won the Game*************")





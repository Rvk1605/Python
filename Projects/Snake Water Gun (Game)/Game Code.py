# Stone Paper Scissor
import time
import random
c = 0
h = 0
print("                             SNAKE    WATER    GUN                            ")
print("Rules")
print("There will be 10 Rouunds in Game ")
print("1.If SNAKE and WATER then Snake Drinks Water and respective Player Wins")
print("2.If SNAKE and GUN then then Gun Kills the Snake and respective Player Wins")
print("3.If Water and Gun Appears Guns Drown in water and respective player wins")
print("RESULT WILL BE DECLARED AT LAST")
print()

for i in range(10):
    lst = ["Snake", "Water", "Gun"]
    n = random.choice(lst)
    l = {'s': "Snake", 'w': "Water", 'g': "Gun"}
    print("Round :",i+1)
    ch = input("Enter (s=Snake || w=Water || g=Gun) s,w,g:")
    m = l[ch]
    if n is m:
        print("Oops!!! It's a Match")
        pass
    elif n == 'Snake' and m == 'water':
        c=c+1
    elif n == 'Gun' and m == 'Snake':
        c=c+1
    elif n == 'Water' and m == 'Gun':
        c=c+1
    else:
        h=h+1
    print("User = ",n)
    print("Computer = ",m)

    print()
print()
print("  Your Score : ",c)
print("  Computer Score : ",h)
if(c>h):
    print("          CONGRATULATIONS            ")
    print("      !!! You Are WINNER !!!       ")
time.sleep(10)
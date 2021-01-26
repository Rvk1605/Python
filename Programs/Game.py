# Stone Paper Scissor
import random
c = 0
h = 0
for i in range(10):
    lst = ["Snake", "Water", "Gun"]
    n = random.choice(lst)
    l = {'s': "Snake", 'w': "Water", 'g': "Gun"}

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
    print("User = ",n,"and Computer = ",m)

    print()
print()
print("  Your Score : ",c)
print("  Computer Score : ",h)
if(c>h):
    print("          CONGRATULATIONS            ")
    print("      !!! You Are WINNER !!!       ")
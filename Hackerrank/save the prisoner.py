
def save():
    n,sweet,seat=map(int, input().split())
    count=0
    if sweet>n:
        count=sweet%n+seat-1
    else :
        count=sweet-1+seat
    return count


tc=int(input())
warn=[]
for i in range(tc):
    warn.append(save())
for i in warn:
    print(i)
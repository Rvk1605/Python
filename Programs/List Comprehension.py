from itertools import permutations
if __name__ == '__main__':
    lst=[]
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    for i in range(3):
        for j in range(3):
                for k in range(3):
                        for l in range(3):
                            lst.append(l)
                            lst=permutations(lst)

    print(lst)

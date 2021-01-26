if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest = 0
    for i in arr:
        if (i > largest):
            largest = i
    for j in range(n):
        for i in arr:
            if(i==largest):
                arr.remove(largest)

    largest = 0
    for i in arr:
        if (i > largest):
            largest = i
    print(largest)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest =max(arr)
    arr=list(dict.fromkeys(arr))
    arr.sort()
    l=arr[len(arr)-2]
    print(l)
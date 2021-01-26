def average(array):
    a=set(array)
    sum=0
    for i in a:
        sum=sum+i
    avg=sum/len(a)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
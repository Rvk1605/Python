if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0
    for j in range(3):
        sum=sum + student_marks[query_name][j]
    print(sum)
    average=sum/3
    print(f"{average:.2f}")

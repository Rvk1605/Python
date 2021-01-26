import array

score = array.array('i', [])
n = int(input())
for i in range(n):
    score.append(int(input()))
large = 0
lar = 0
for j in range(n):
    if score[j] > large:
        large = score[j]
for j in range(len(score)):
    if ((score[j] > lar) and (score[j] < large)):
        lar = score[j]
print(lar)

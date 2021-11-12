n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
for j in range(n) :
    score[j] = score[j] / max_score * 100
print(sum(score)/n)
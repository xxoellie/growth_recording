n = int(input())

for i in range(n):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    cnt = 0
    for j in score[1:]:
        if avg < j :
            cnt += 1

    print("{:.3f}%".format((cnt/score[0])*100))
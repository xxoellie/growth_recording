for i in range(int(input())):
    cnt = 0
    sum = 0
    ox = list(input())
    for j in ox :
        if j == "O" :
            cnt += 1
            sum += cnt
        else :
            cnt = 0
    print(sum)
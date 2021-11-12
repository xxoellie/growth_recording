N, K = list(map(int,input().split()))
coin_list = []
for _ in range(N) :
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

cnt = 0
for i in coin_list :
    if K == 0:
        break
    cnt += K//i
    K %= i

print(cnt)

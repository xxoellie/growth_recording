# 처음에 접근했던 방식
M,N = map(int,input().split())
n = N + 1
sieve = [True] * n
m = int(n**0.5)
for i in range(2,m+1):
    if sieve[i] == True:
        for j in range(2*i, n, i):
            sieve[j] = False
for i in range(M,N+1):
    if sieve[i] == True :
        print(i)


# 두번째로 푼 방식
M,N = map(int,input().split())
for i in range(M,N+1) :
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else :
        print(i)
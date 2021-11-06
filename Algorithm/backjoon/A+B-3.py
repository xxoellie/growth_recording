N = int(input())

for i in range(N) :
    num = list(map(int, input().split()))
    print(sum(num))
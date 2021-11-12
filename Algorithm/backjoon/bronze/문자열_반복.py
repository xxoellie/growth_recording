n = int(input())
for i in range(n):
    R,S = list(input().split())
    words = ''
    for j in S :
        words += j * int(R)
    print(words)
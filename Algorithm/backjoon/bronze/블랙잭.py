from itertools import combinations

N,M = map(int,input().split())
lst = list(map(int,input().split()))
a = list(combinations(lst,3))

blackjack = []
for i in range(len(a)):
    b = sum(a[i])
    if b <= M :
        blackjack.append(b)
print(max(blackjack))

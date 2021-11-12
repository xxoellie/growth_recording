from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n) :
    [a,b] = list(map(int,input().split()))
    lst.append([a,b])

lst.sort()

for j in lst :
    print(j[0],j[1])
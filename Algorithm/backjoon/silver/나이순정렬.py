n = int(input())
user = []
for _ in range(n):
    user.append(list(input().split()))

user.sort(key=lambda a : int(a[0]))

for i in user :
    print(i[0],i[1])
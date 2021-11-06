#min이랑 max값을 사용한 방법
a = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))

#min max를 활용하지 않은 방법
cnt = int(input())
num = list(map(int, input().split()))
max = num[0]
mix = num[0]
for i in num[1:]:
    if i > max :
        max = i
    elif i < min :
        min = i
print(min, max)
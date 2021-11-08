num = int(input())
while True :
    n = 0
    if num >= (3*(n**2)-3*n+2) and num <= (3*(n**2)-3*n+7):
        break
    else :
        n += 1
print(n+1)

for i in range(1000000001):
    if num >= (3*(i**2)-3*i+2) and num <= (3*(i**2)-3*i+7):
        break
print(i+1)

N = int(input())
cnt = 1
while N > 1:
    N -= (6 * cnt)
    cnt += 1
print(cnt)
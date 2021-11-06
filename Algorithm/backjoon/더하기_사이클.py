n = int(input())
num = n
cnt = 1
while True :
    sum = (num // 10) + (num % 10)
    num = (num % 10) * 10 + (sum % 10)
    if num != n:
        cnt += 1
    else:
        break
print(cnt)
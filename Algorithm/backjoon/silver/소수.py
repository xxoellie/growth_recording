from sys import stdin
m = int(stdin.readline())
n = int(stdin.readline())

prime_list = []
sum = 0
for i in range(m, n+1):
    if i == 1 :
        continue
    for j in range(2,int(i**0.5)+1) :
        if i%j == 0 :
            break
    else :
        sum += i
        prime_list.append(i)

if len(prime_list) == 0 :
    print("-1")

else :
    print(sum)
    print(min(prime_list))


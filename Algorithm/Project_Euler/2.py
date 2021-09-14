n = list(map(int,input().split(" ")))

sum = 0
while True:
    a = n[-1] + n[-2]
    n.append(a)
    if a >= 4000000:
        break

for i in n :
    if i % 2 == 0 :
        sum += i
print(sum)
# 피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?

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
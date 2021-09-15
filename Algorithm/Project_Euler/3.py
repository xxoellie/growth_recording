# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.
#
# 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

# 처음에 생각한 방법
N = int(input(""))
quotient = []
list=[]
for i in range(2,N+1):
  if N%i == 0:
    quotient.append(i)

# 임의의 수를 약수를 먼저 구해서 그 약수에서 소수를 판별하면 된다고 생각

for j in quotient:
    while N%j==0 :
        N = N/j
        list.append(j)
print(list[-1])

# 그래서 구한 약수에서 while 문 진행하니까 속도가 너무 느림


# 두 번째 생각한 방법
def solution(x):
    d = 2
    lst = []
    while d <= x :
        if x%d == 0 :
            lst.append(d)
            x = x/d

        else :
            d = d+1
    return lst[-1]

a = solution(600851475143)
print(a)

# 약수를 구할 필요 없이 while 문에서 모든 과정을 진행하는 것으로 접근법을 바꿔봄

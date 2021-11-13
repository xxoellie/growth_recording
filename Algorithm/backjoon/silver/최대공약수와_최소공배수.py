a,b = list(map(int,input().split()))
# 최대공약수
for i in range(min(a,b),0,-1) :
    if a%i == 0 and b%i == 0 :
        print(i)
        break
"""
a,b 중 가장 작은 숫자부터 1까지 -1을 하며 for문을 실행시킵니다.
만약 a%i, b%i 값이 모두 딱 떨어져서 나머지가 없는 상태라면 이 때 사용된 i는 a와 b와 최대 공약수입니다.
"""

# 최소공배수
for i in range(max(a,b),(a*b)+1):
    if i%a==0 and i%b==0 :
        print(i)
        break
"""
a,b 중 더 큰 숫자부터 a*b의 수까지 for문을 실행시킵니다. 
더 큰 숫자부터 실행하는 이유는 a,b의 배수들 중에서 공통부분을 찾는 것이기 때문에 a,b 중 작은 수부터 시작하게되면
i가 +1이 되면서 큰 수에 도달할 때까지 for문은 헛돌게 됩니다.
"""

import math

a, b = map(int, input().split())
print(math.gcd(a,b), math.lcm(a,b))
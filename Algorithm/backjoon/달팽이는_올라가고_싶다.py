# 처음에 생각한 방법 시간 초과
A,B,V = list(map(int,input().split()))
n = 1
while True :
    V = V - A  # 달팽이가 낮에 올라가는 만큼
    if V > 0 :
        n+=1
        V += B
    else :
        break
print(n)

# 단위가 클 수 있기 때문에 수학적으로 접근해야한다.

import math

A, B, V = map(int, input().split())
# A = 낮에 올라간 거리, B = 밤에 미끄러진 거리, V = 나무 막대의 높이

crawl = math.ceil((V-B) / (A-B))
#  나무 높이 V에서 정상에 도달 후 미끄러지지 않는 B를 빼면 매일 (A-B)만큼씩 올라가게 된다.
# 수식을 정리하면, 달팽이는 (V-B) / (A-B)일 동안 올라가게 된다.
# 마지막 날은 조금만 올라도 하루가 지난 것으로 치니 소숫점이 나오게 되면 ceil로 올림 처리해 하루를 더 세준다.


print(crawl)
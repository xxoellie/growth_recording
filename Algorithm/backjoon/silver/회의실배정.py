n = int(input())
time = []
for _ in range(n) :
    start, end = map(int,input().split())
    time.append([start,end])
"""
주어진 시작시간과 끝나는 시간들을 이용해서 가장 많은 회의의 수를 알기 위해서는 빨리 끝나는 회의순서대로 정렬을 해야함
이유는 빨리 끝낼수록 뒤에서 고려해볼 회의가 많기 때문
빨리 시작하는 순서대로 정렬을 우선시 한다면 오히려 늦게 끝날 수 있다.

그래서 먼저 시작시간을 오름차순으로 정렬한 뒤, 끝나는 시간을 기준으로 한 번 더 정렬을 해야한다.
"""
time = sorted(time, key=lambda a : a[0])
time = sorted(time, key=lambda a : a[1])

print(time)
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
last = 0 # 회의의 마지막 시간을 저장할 변수
count = 0 # 회의 개수를 저장할 변수

for i, j in time :
    if i >= last : # 시작시간이 회의의 마지막 시간보다 크거나 같을 경우
        count += 1
        last = j

print(count)
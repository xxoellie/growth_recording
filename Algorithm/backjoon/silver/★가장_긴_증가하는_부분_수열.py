#Dynamic Programming 풀이법

x = int(input()) # 수열 A의 크기

arr = list(map(int, input().split())) # 수열 A를 이루고 있는 A(i)를 담은 배열

dp = [1 for i in range(x)] # arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

"""
dp[i]의 값을 1로 초기화
현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인한다(크거나 같으면 가장 긴 증가하는 부분 수열이 될 수가 없음)
작다면, 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해준다
"""
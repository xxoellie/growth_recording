"""
브루트 포스는 거의 모든 문제에서 사용할 수 있는 기법으로 완전 탐색이라고 합니다.
이 기법은 이름처럼 맹목적으로 모든 경우의 수를 탐색하여 결과를 도출하는 기법입니다.
모든 경우의 수를 탐색해 봐야만 하는 경우나 모든 경우의 수를 요구하는 문제에서 주로 사용됩니다.
"""

# 부르트 포스 알고리즘 파이썬 코드
# 비교 대상 문자열의 끝까지 비교하거나 패턴을 찾을 때까지 반복해서 문자를 하나씩 차례로 비교합니다.
# 원본 문자열에서 패턴이 속한 시작 위치를 반환합니다.

# def BruteForce(p,t) :
#   i = 0 # t의 검색 인덱스
#   j = 0 # p의 검색 인덱스
#
#   while i < len(t) and j < len(p) :
#     if t[i] != p[j] :
#       i = i - j
#       j = -1
#     i += 1
#     j += 1
#   if j == len(p) :
#     return i - len(p)
#   else :
#     return -1

n,m = map(int,input().split())
lst = []

for _ in range(n):
  lst.append(input())

original = []
count = []
for a in range(n-7) : # 전체 체스판에서 시작점을 잡기 위한 반복문(a는 행, b는 열)
  for b in range(m-7):
    index1 = 0 # 'W'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함
    index2 = 0 # 'B'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함

    # 행과 열의 시작점 a,b를 기준으로 8칸씩 모두 체크한다
    # 현재 행의 번호 i, 현재 열의 번호 j의 합이 짝수이면 시작점의 색깔과 같아야 하고, 홀수이면 시작점의 색깔과 다른 색이어야 한다.
    # 이를 이용하여 만약 i+j의 합이 짝수일 경우
    # W가 아니라면 index1에 1을 더하고, B가 아니라면 index2에 1을 더한다.
    # else문은 i+j의 합이 홀수인 경우로, 시작점의 색깔과 다르지 않은 경우를 체크합니다.
    for i in range(a, a+8) :
      for j in range(b,b+8) :
        if (i+j) % 2 == 0 :
          if original[i][j] != 'W' :
           index1 += 1
          if original[i][j] != 'B' :
           index2 += 1
        else :
          if original[i][j] != 'B' :
           index1 += 1
          if original[i][j] != 'W' :
           index2 += 1
      count.append(min(index1, index2))

print(min(count))
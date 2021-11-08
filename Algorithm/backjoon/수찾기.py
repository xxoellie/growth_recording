# 직관적으로 생각해서 풀었더니 시간 초과가 났다.
# n,m이 1부터 10만 사이로 주어지기 때문에 이런 탐색법은 시간이 오래걸릴 수 밖에 없음
# list의 search는 0(n) 직선적 시간으로 처음부터 원하는 값이 나올 때까지 if문을 돌릴 때 순차탐색을 하고
# set의 search는 0(1) 상수 시간으로 알고리즘이 문제를 해결하는데 오직 한 단계만 거치게 됨
from sys import stdin
n = int(stdin.readline())
n_lst = set(map(int, stdin.readline().split()))
m = int(stdin.readline())
m_lst = list(map(int, stdin.readline().split()))
for i in range(m):
    if m_lst[i] in n_lst :
        print("1")
    else :
        print("0")
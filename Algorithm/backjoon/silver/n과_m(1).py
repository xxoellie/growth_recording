import itertools

n,m = map(int,input().split())

lst = [int(i) for i in range(1,n+1)]

a = list(itertools.permutations(lst,m))
for i in a :
    print(' '.join(map(str,i)))
    print(*i)


"""
백트래킹(https://jamesu.dev/posts/2020/04/13/baekjoon-problem-solving-15649/)
백트래킹은 DFS의 방식을 기반으로 불필요한 경우를 배제하며 원하는 해답에 도달할 때까지 탐색하는 전략입니다.
dfs를 기반으로 두고 있기 때문에 스택을 이용해 퇴각을 하며 다음 탐색을 진행하기 때문에 백트래킹이라 불린다.
백트래킹은 기본적으로 모든 경우의 수를 탐색한다는 브루트 포스 전략을 취하지만 처리 속도를 향상시키기 위한 가지치기가 중요한 역할을한다.
나무에서 불필요한 가지를 제거하듯이 백트레킹에서 가지치기를 잘 할수록 불필요한 경우가 제거되어 처리 속도가 많이 향상됩니다.
반복적으로 숫자를 선택해 m개까지 골라 수열을 완성하는 것이 목표
따라서 백트래킹을 적용해 불필요한 경우를 배제한 모든 경우의 수를 고려할 수 있다.
숫자를 선택할 때 1부터 n까지의 자연수 중 선택해야 하므로 차례대로 선택하는 경우의 수가 있을 것이다.
이 때 반드시 해당 경우의 수를 스택에 추가(push)하고, 동작이 끝난 후에는 다시 스택에서 빼내는 작업이 필요하다.
"""

n, m = map(int, input().split())

def f(s):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    f(s + [i])

f([])

#강상연 유튜브 코드 https://www.youtube.com/watch?v=c_xgtl0W8Fo

import sys
def dfs(end, max_depth, current_stack) :
  for i in range(1,end+1) :
    if i in current_stack:
      continue

    current_stack.append(i)

    if len(current_stack) == max_depth :
      print(*current_stack)
    else :
      dfs(end,max_depth, current_stack)

    current_stack.pop()

end, max_depth = [int(value) for value in sys.stdin.readline().rstrip().split()]
stack = list()
dfs(end,max_depth,stack)
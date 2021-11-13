n = int(input())
lst = [i for i in range(1,n+1)]
while len(lst)>1 :
    lst.pop(0)
    temp = lst.pop(0)
    lst.append(temp)
    print(lst)

print(lst.pop(0))

"""
시간초과를 줄일 수 있는 방법 
from collections import deque 활용
양쪽 끝에서 삽입과 삭제가 모두 가능한 자료 구조
큐와 스택을 합친 형태와 비슷
"""
from collections import deque
N = int(input())
deque = deque([i for i in range(1, N+1)])
while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])

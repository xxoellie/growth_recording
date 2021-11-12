# 메모리가 8 MB로 제한되어 있으므로 그 점에 유의해서 풀어야한다
from sys import stdin
n = int(stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(stdin.readline()))
print(sorted(lst),end='\n')

# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용하지 못한다
# 일반적으로 입력값이 크지 않은 경우에는 상관없지만 이렇게 입력값이 극한으로 많이 주어질 때에는 메모리를 효율적으로 관리해야합니다.


n = int(stdin.readline())
num_list = [0] * 10001
for _ in range(n):
    num_list[int(stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
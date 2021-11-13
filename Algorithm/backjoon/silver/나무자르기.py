from sys import stdin
n,m = map(int,stdin.readline().split())
tree_list = list(map(int,stdin.readline().split()))
start, end = 1, max(tree_list) #가장 짧은 길이 1을 start, 나무 중 가장 긴 길이를 end로 둔다.

while start <= end : #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2 #mid를 start와 end의 중간으로 두고 모든 값에서 mid를 빼 총 어느 정도 길이의 벌목된 나무나 나오나 살펴본다.

    # 벌목나무가 목표치 이상이면 mid+1을 start로 두고 while문 반복
    # 벌목나무가 목표치 이하면 mid-1을 end로 두고 다시 while문 반복
    log = 0 #벌목된 나무 총합
    for i in tree_list :
        if i > mid :
            log += i - mid

    if log >= m :
        start = mid +1
    else :
        end = mid - 1

print(end)
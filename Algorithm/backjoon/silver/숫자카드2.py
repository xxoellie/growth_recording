# from sys import stdin
# n = int(stdin.readline())
# card_list = list(map(int,stdin.readline().split()))
# m = int(stdin.readline())
# count_list = list(map(int,stdin.readline().split()))
#
#
# for j in count_list :
#     print(card_list.count(j),end=" ")


#자료구조, 이분탐색,해시를 사용해 집합과 맵

n = int(input())
arr1 = list(map(int,input().split()))
#6 3 2 10 10 10 -10 -10 7 3

dict1 = dict()

#숫자카드와 개수를 딕셔너리에 담기
for i in arr1 :
    if i in dict1 :
        dict1[i] += 1
    else :
        dict1[i] = 1

m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2 :
    if i in dict1 :
        print(dict1[i], end=' ') # 존재하는 숫자 카드라면
    else :
        print(0, end=' ')

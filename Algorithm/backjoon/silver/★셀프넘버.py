#1부터 10000까지 숫자 저장
num_set = set(range(1,10001))

# 셀프 넘버가 아닌 수를 저장
not_self_num = set()

for i in range(1,10001):
    for j in str(i): # 숫자를 문자열로 변환하여 102면 1,0,2로 접근
        i +=int(j) # d(i) = 102 + 1 + 0 + 2

    not_self_num.add(i) # 셀프넘버가 아닌 수 저장

self_num = num_set - not_self_num

for i in sorted(self_num):
    print(i)
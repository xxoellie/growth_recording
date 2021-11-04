# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
#
# 이 때 10,001번째의 소수를 구하세요.

# lst = []
# for i in range(2,100000000):
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
#         lst.append(i)
#
#
# print(lst[])

# lst =[]
# def prime(x):
#     for i in range(2,x+1):
#         for j in range(2,i):
#             if i % j == 0 :
#                 break
#             else :
#                 lst.append(i)
#     return lst[10000]
#
# a=prime(10000000)
# print(a)

# def prime_list(n):
#     sieve = [True] * n
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:
#             for j in range(2*i, n, i):
#                 sieve[j] = False
#
#     return [i for i in range(2, n) if sieve[i] == True]
#
# a = prime_list(10000000)
# print(a[10000])


prime_lst =[2,3,5,7]
i = prime_lst[-1]+1
while len(prime_lst)<10001:
    cnt = 0
    for j in prime_lst:
        if i % j ==0:
            i+=1
            break
        else:
            cnt +=1
    if cnt == len(prime_lst):
        prime_lst.append(i)
        i += 1
print(prime_lst[-1])
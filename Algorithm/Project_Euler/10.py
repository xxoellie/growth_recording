# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
#
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

def prime(n):
    vector = [True] * n
    m = int(n**0.5)
    sum = 0
    for i in range(2,m+1):
        if vector[i] == True :
            for j in range(2*i,n,i):
                vector[j] = False
    return [i for i in range(2,n) if vector[i] == True]

a = prime(2000000)
print(sum(a))

# sum=0
# for i in range(2,n):
#     if vector[i]==True:
#         sum += [i]
#


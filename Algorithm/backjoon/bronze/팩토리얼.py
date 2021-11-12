n = int(input())
mul = 1
for i in range(1,n+1):
    if n == 0 :
        print(1)
    else :
        mul *= i
print(mul)
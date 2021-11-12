# num1 = 0
# num2 = 1
# for i in range(int(input())-2):
#     num1 , num2 = num2, num1+num2
#     pibo = num1 + num2
# print(pibo)


n = int(input())
fibo= [0,1]
for i in range(2,n+1):
    num = fibo[i-1] + fibo[i-2]
    fibo.append(num)

print(fibo[n])
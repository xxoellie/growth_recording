n = list(map(int,input().split()))
lst = []
for i in n :
    i = list(str(i))
    i.reverse()
    lst.append(''.join(i))
print(max(lst))


num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)
n = int(input())

for i in range(1,n+1):
    num = sum(map(int,str(i)))
    new_num = i + num
    if new_num == n :
        print(i)
        break
    if i == n :
        print(0)
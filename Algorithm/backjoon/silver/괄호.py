n = int(input())
for _ in range(n) :
    a = list(input())
    sum = 0
    for i in range(len(a)) :
        if a[i] == "(" :
            sum+=1
        else :
            sum -= 1
        if sum<0 :
            print("NO")
            break

    if sum > 0 :
        print("NO")
    elif sum == 0 :
        print("YES")
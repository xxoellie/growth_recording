n = int(input())
for i in range(n) :
    A,B = map(int,input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, A,B,A+B))
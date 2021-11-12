from sys import stdin
while True :
    a,b,c = map(int,stdin.readline().split())
    if a==0 and b==0 and c==0 :
        break
    num_list = [a,b,c]
    num_list.sort()
    if (num_list[2]**2) == (num_list[0]**2)+(num_list[1]**2):
        print("right")
    else :
        print("wrong")
n = int(input())
for i in range(n):
    H, W, N = list(map(int, input().split()))

    if N%H == 0:
        room_num = H * 100 + (N // H)
    else:
        room_num = N % H * 100 + ((N // H) + 1)

    print(room_num)
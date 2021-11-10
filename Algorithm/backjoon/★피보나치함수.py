n = int(input())


for _ in range(n):
    fibo0 = [1,0]
    fibo1 = [0,1]
    num = int(input())
    if num > 1 :
        for i in range(num-1):
            fibo0.append(fibo1[-1])
            fibo1.append(fibo0[-2]+fibo1[-1])

    print(fibo0[num], fibo1[num])

# 0의 갯수 = 이전 1의 갯수, 1의 갯수 = 이전 0+이전 1 갯수
# 기본으로 0과 1일 때 갯수를 초기화시키기
# 0과 1인 경우는 이미 리스트에 있으므로 1보다 클 경우만 진행
# 현재 0의 갯수는 이전 1의 갯수를 가져온다
# 현재 1의 갯수는 이전 0의 갯 + 이전 1의 갯수
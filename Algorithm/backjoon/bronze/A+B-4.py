# 처음 풀이 A+B-5에서 했던 방법 그대로 가져다 썼더니 런타임에러가 뜸

for i in range(100000):
    A, B = map(int, input().split())
    print(A+B)

# 내가 이제껏 쓰지 않았던 try~except 구문을 사용
while True :
    try :
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
# 입력 개수에 제한이 없으므로 try~except으로 풀면 두 수가 입력되지 않는 경우에는 반복문이 끝난다
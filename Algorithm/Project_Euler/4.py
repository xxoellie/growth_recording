# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
#
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
#
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

lst = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if str(i*j) == str(i*j)[::-1]:
            lst.append(i*j)

print(max(lst))

# 접근은 해봤지만 숫자를 어떻게 대칭하는지 몰라서 해맸다..ㅎㅎ
# str(i*j)[::-1] 메모메모!


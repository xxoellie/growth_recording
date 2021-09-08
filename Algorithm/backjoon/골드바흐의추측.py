def isPrime(n):
    numbers = [1] * n

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i] == 1:
            for j in range(i + i, n, i):
                numbers[j] = 0
    return numbers

numbers = isPrime(100000)

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, (n // 2) + 1):
        if numbers[i] and numbers[n - i]:
            print("{}={}+{}".format(n, i, n - i))
            break
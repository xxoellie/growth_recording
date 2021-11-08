n = int(input())
for i in range(n):
    word = input()
    for j in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            n -= 1
            break
print(n)
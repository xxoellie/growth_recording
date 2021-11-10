n = int(input())
word_list = []
for i in range(n) :
    word_list.append(input())

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=len)

for j in word_list :
    print(j)


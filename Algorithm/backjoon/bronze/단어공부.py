a = list(str(input()).upper())
b = list(set(a))
count_list = []
for i in b :
    count_list.append(a.count(i))
max = max(count_list)
index = count_list.index(max)
if count_list.count(max) > 1 :
    print("?")
else :
    print(b[index])
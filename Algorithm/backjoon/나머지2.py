lst = []
for i in range(10):
    lst.append(int(input())%42)
count = set(lst)
print(len(count))
# cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
# s = str(input())
# lst = []
# for i in cro :
#     print(s.find(i))
#     if s.find(i) >= 0 :
#         lst.append(i)
# print(lst)
#
# for j in range(len(lst)):
#     s = s.replace(lst[j], "")
#
# print(len(s)+len(lst))

cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
s = str(input())
cnt = 0

for i in cro :
    if i in s :
        cnt += s.count(i)

print(len(s)-cnt)

alpha="abcdefghijklmnopqrstuvwxyz"
string = input()
print(string)
# for i in string :
#     for j in range(len(alpha)):
#         if i in alpha :
#             alpha[j] = string.index(i)
#         else :
#             alpha[j] = "-1"
# print(alpha)

for i in alpha :
    if i in string :
        print(string.index(i), end=' ')
    else :
        print("-1", end=' ')

for i in alpha :
    print(string.find(i), end=' ')
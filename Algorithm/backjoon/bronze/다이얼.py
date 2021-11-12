# phone_num = input()
# num =  ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# sum = 0
# for i in range(len(phone_num)):
#     for j in num :
#         if phone_num[i] in j :
#            sum += num.index(i)+3
#
# print(sum)


dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sum = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            sum += dial.index(i)+3
print(sum)

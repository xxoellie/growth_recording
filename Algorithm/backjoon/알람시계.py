# def alarm(H,M) :
#     if H > 0 :
#         if M - 45 < 0:
#             H = H - 1
#             M = 60 + (M - 45)
#         else :
#             M - 45
#     else :
#         if M - 45 < 0:
#             H = 24+(H-1)
#             M = 60 + (M - 45)
#         else :
#             M - 45
#     return H,M
#
# a = alarm(10,10)
# b = alarm(0,30)
# c = alarm(23,40)
#
# print(a)
# print(b)
# print(c)

H,M = map(int, input().split())
def alarm(H,M) :

    if H > 0 and M < 45 :
        H = H - 1
        M = M + 15
    elif M >= 45:
        M = M-45
    else :
        print(23,M+15)

    return H,M
a = int(input())
b = int(input())

c = b % 100

print(a * (b%10))
print(a * (c//10))
print(a * (b//100))
print(a*b)
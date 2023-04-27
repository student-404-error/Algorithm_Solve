a, b = map(int, input().split())
if a < b:
    a, b = b, a

mod = 1
x = a * b

while mod != 0:
    mod = a % b
    a = b
    b = mod
print(a)
print((x//a))


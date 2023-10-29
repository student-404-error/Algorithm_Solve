import sys

input = sys.stdin.readline
a2, a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
flag = True

a = a2 - c
s = int((-a1 * (a1**2 - 4 * a * a0) ** 1 / 2) / (2 * a))
e = int((-a1 * (a1**2 + 4 * a * a0) ** 1 / 2) / (2 * a))

# print(s, e)
if s > e:
    s, e = e, s


def calcfg(n: int):
    fn = (a2 * (n**2)) + (a1 * n) + a0
    cgn = c * (n**2)
    return fn, cgn


for i in range(s, e, 1):
    f, g = calcfg(n0)
    if g > f:
        flag = False
        break
print(int(flag))

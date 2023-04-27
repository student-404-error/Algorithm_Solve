from itertools import combinations

# a = list(combinations(range(100), 6))
a, b = map(int,input().split())
# print(len(a))
s = 1
c = 1
for i in range(a, a-b, -1):
    s = s * i
for i in range(b, 1, -1):
    c = c * i
print(s//c)
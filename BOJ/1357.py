# 뒤집힌 덧셈
"""
x = 321
Rev(x) => 123
"""

a, b = map(str, input().split())
a = list(reversed(a))
b = list(reversed(b))
s = 0

for idx, val in enumerate(a):
    s = s + int(val) * (10**(len(a) - 1 - idx))

for idx, val in enumerate(b):
    s = s + int(val) * (10**(len(b) - 1 - idx))


s = list(reversed(str(s)))

result = 0
for idx, val in enumerate(s):
    result = result + int(val) * (10**(len(s) - 1 - idx))

print(result)
# int(s)
# print(s)



# for i in range(len(a)):
#     rev_a.append(a.pop())

# for i in range(len(b)):
#     rev_b.append(b.pop())
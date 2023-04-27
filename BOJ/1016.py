from math import sqrt

n, m = map(int, input().split())
dec = [True] * (m + 1 - n)

ms = int(sqrt(m))

for i in range(2, ms+1, 1):
    for j in range(i*i, m+1, i*i):
        if n <= j <= m:
            dec[j - n] = False

print(dec.count(True))

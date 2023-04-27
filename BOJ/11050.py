import sys
input = sys.stdin.readline
N, K = map(int, input().split())

s = 1
a = 1
for i in range(K):
    s = s * (N - i)

for i in range(2, K+1):
    a *= i
print((s//a)%1000000007)
# 요세푸스 문제
# (N, K)
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
# A = [(i % N)+1 for i in range(N+1, 1, -1)]
# print(A)
# q = deque([(i % (N))+1 for i in range(K-1, N+K-1)])
# q = deque([(i % N)+1 for i in range(N+1, 1, -1)])
q = deque([i for i in range(N, 0, -1)])
result = []
for i in range(len(q)):
    q.rotate(K-1)
    result.append(q.pop())
    # print("now q :", q)

print("<", end='')
print(', '.join(map(str, result)), end='')
print(">")

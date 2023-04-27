# 너비 우선 탐색
from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
A = [[] for _ in range(n+1)]

visited = [False] * (n + 1)
result = []

# 양방향 그래프니까 둘다 추가
for i in range(m):
    ed1, ed2 = map(int, input().split())
    A[ed1].append(ed2)
    A[ed2].append(ed1)

for _ in range(n+1):
    A[_].sort()


def DFS(now):
    result.append(now)
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i)


DFS(v)
print(*result)
visited = [False] * (n + 1)
result = []

q = deque()


def BFS(now):
    q.appendleft(now)
    while len(q) != 0:
        now = q.pop()
        result.append(now)
        visited[now] = True
        for i in A[now]:
            if (not visited[i]) and (i not in q):
                q.appendleft(i)


BFS(v)
print(*result)

# DFS

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if visited[i] == False: # not visited
            DFS(i)

for i in range(m):
    ed1, ed2 = map(int, input().split())
    # 방향이 없는 그래프라 양쪽 노드에 엣지(간선) 추가
    A[ed1].append(ed2)
    A[ed2].append(ed1)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        DFS(i)
print(cnt)
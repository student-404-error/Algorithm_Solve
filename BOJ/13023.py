import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n)]

visited = [False] * (n + 1)
arr = False

for i in range(m):
    ed1, ed2 = map(int, input().split())
    A[ed1].append(ed2)
    A[ed2].append(ed1)


def DFS(node: int, depth: int) -> None:
    global arr
    if depth == 5:
        arr = True
        return
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[node] = False


for i in range(n):
    DFS(i, 1)
    if arr:
        break
if arr:
    print(1)
else:
    print(0)

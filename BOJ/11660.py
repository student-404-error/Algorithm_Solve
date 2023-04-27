#11660 - 구간 합 구하기 5
""" 예제
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

A = [[0]*(N+1)]
D = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    A.append([0] + list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        D[i+1][j+1] = A[i+1][j+1] + D[i][j+1] + D[i+1][j] - D[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2]-D[x1 - 1][y2] - D[x2][y1-1] + D[x1-1][y1-1])
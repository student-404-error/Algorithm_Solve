# 공 바꾸기

import sys
input = sys.stdin.readline


def swap(x: int, y: int, arr: list) -> None:
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp


n, m = map(int, input().split())
board = [i for i in range(1, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    swap(a-1, b-1, board)
    # board[a - 1], board[b - 1] = board[b - 1], board[a - 1]


print(*board)

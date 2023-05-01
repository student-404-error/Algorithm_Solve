# 바구니 뒤집기

import sys
input = sys.stdin.readline


def swap(x: int, y: int, arr: list) -> None:
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp


n, m = map(int, input().split())
board = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    while i <= j:
        swap(i-1, j-1, board)
        i += 1
        j -= 1

print(*board)

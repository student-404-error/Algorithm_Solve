import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    board[i-1:j] = [k]*(j-i+1)

print(*board)

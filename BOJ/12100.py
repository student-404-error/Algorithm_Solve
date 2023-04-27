import sys
from pprint import pprint
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
trans_board = [[False] * N for _ in range(N)]

# print(trans_board)
# print(*board)


def left():
    global trans_board
    for i in range(0, N):
        for j in range(1, N):
            trans_board = [[False] * N for _ in range(N)]
            move_left(i, j)
            # print(board[i][j])


def move_left(i, j):
    if board[i][j-1] == board[i][j]:
        if not trans_board[i][j-1]:
            board[i][j-1] += board[i][j]
            board[i][j] = 0
            trans_board[i][j-1] = True
    elif board[i][j-1] != 0:
        return
    elif board[i][j-1] == 0:
        board[i][j-1] = board[i][j]
        board[i][j] = 0
        move_left(i, j-1)  # 끝까지 옮겨야함.


move_left(0, 1)
move_left(0, 2)

print(board)

import sys
input = sys.stdin.readline

s = int(input())
m = input()
move = []
for i in range(4, len(m), 4):
    move.append([m[i-4], m[i-3:i]])

trans_board = [[False] * 4 for _ in range(4)]
board2 = list(map(int, input().split()))
board = []
for i in range(4, len(board2)+1, 4):
    board.append(board2[i-4:i])


def left():
    global trans_board
    for i in range(0, 4):
        for j in range(1, 4):
            trans_board = [[False] * 4 for _ in range(4)]
            move_left(i, j)


def move_left(i, j):
    global s
    if j <= 0:
        return
    elif board[i][j-1] == board[i][j]:
        if not trans_board[i][j-1]:
            board[i][j-1] += board[i][j]
            board[i][j] = 0
            trans_board[i][j-1] = True
            s += board[i][j-1]
    elif board[i][j-1] != 0:
        return
    elif board[i][j-1] == 0:
        board[i][j-1] = board[i][j]
        board[i][j] = 0
        move_left(i, j-1)  # 끝까지 옮겨야함.


def right():
    global trans_board
    for i in range(0, 4):
        for j in range(2, -1, -1):
            trans_board = [[False] * 4 for _ in range(4)]
            move_right(i, j)


def move_right(i, j):
    global s
    if j >= 3:
        return
    elif board[i][j+1] == board[i][j]:
        if not trans_board[i][j+1]:
            board[i][j+1] += board[i][j]
            board[i][j] = 0
            trans_board[i][j+1] = True
            s += board[i][j+1]
    elif board[i][j+1] != 0:
        return
    elif board[i][j+1] == 0:
        board[i][j+1] = board[i][j]
        board[i][j] = 0
        move_right(i, j+1)  # 끝까지 옮겨야함.


def up():
    global trans_board
    for i in range(1, 4):
        for j in range(0, 4):
            trans_board = [[False] * 4 for _ in range(4)]
            move_up(i, j)


def move_up(i, j):
    global s
    if i <= 0:
        return
    elif board[i-1][j] == board[i][j]:
        if not trans_board[i-1][j]:
            board[i-1][j] += board[i][j]
            board[i][j] = 0
            trans_board[i-1][j] = True
            s += board[i-1][j]
    elif board[i-1][j] != 0:
        return
    elif board[i-1][j] == 0:
        board[i-1][j] = board[i][j]
        board[i][j] = 0
        move_up(i-1, j)  # 끝까지 옮겨야함.


def down():
    global trans_board
    for i in range(2, -1, -1):
        for j in range(0, 4):
            trans_board = [[False] * 4 for _ in range(4)]
            move_down(i, j)


def move_down(i, j):
    global s
    if i >= 3:
        return
    elif board[i+1][j] == board[i][j]:
        if not trans_board[i+1][j]:
            board[i+1][j] += board[i][j]
            board[i][j] = 0
            trans_board[i+1][j] = True
            s += board[i+1][j]
    elif board[i+1][j] != 0:
        return
    elif board[i+1][j] == 0:
        board[i+1][j] = board[i][j]
        board[i][j] = 0
        move_down(i+1, j)  # 끝까지 옮겨야함.


def create(n, x, y):
    board[int(x)][int(y)] = int(n)


for mv, xy in move:
    # print(mv)
    # print(xy[0], xy[1], xy[2])
    if mv == "L":
        left()
        create(xy[0], xy[1], xy[2])
        # print(board)
    elif mv == "R":
        right()
        create(xy[0], xy[1], xy[2])
        # print(board)

    elif mv == "U":
        up()
        create(xy[0], xy[1], xy[2])
        # print(board)
    elif mv == "D":
        down()
        create(xy[0], xy[1], xy[2])
        # print(board)


print(s)

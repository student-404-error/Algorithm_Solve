import sys
input = sys.stdin.readline
board = []


def one_check(a, b):
    global board
    board = []
    while True:
        if a > b:
            board.append(a // b)
            a = a % b
        else:
            board.append(b // a)
            b = b % a
        if a == 0 or b == 0:
            break


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b == a:
        print("A wins")
        continue
    one_check(a, b)
    for idx, val in enumerate(board):
        if val != 1:
            if idx % 2 == 0:
                print("A wins")
            else:
                print("B wins")
            break

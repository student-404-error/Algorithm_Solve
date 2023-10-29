import pprint

N, M, R = map(int, input().split())
brd = [list(map(int, input().split())) for i in range(N)]
cmd = list(map(int, input().split()))
new_brd = []


def one():
    for i in range(N // 2):
        brd[i], brd[N - 1 - i] = brd[N - 1 - i], brd[i]


def two():
    for i in range(N):
        brd[i] = brd[i][::-1]


def three():
    for i in range(M):
        a = []
        for j in range(N - 1, -1, -1):
            a.append(brd[j][i])
        new_brd.append(a)
    return new_brd
    # N, M = M, N


def four():
    for i in range(M - 1, -1, -1):
        a = []
        for j in range(N):
            a.append(brd[j][i])
        new_brd.append(a)
    return new_brd


def five():
    # for i in range(N // 2):
    #     tmp = brd[i][: M // 2]
    #     brd[]
    #     print(tmp)
    # for i in range()
    for i in range(N // 2):
        a = []
        a = brd[i + (N // 2)][: M // 2] + brd[i][: M // 2]
        new_brd.append(a)
    for i in range(N // 2):
        a = []
        a = brd[i + (N // 2)][M // 2 :] + brd[i][M // 2 :]
        new_brd.append(a)
    return new_brd


def six():
    for i in range(N // 2):
        a = []
        a = brd[i][M // 2 :] + brd[i + (N // 2)][M // 2 :]
        new_brd.append(a)
    for i in range(N // 2):
        a = []
        a = brd[i][: M // 2] + brd[i + (N // 2)][: M // 2]
        new_brd.append(a)
    return new_brd


for i in cmd:
    if i == 1:
        one()
    elif i == 2:
        two()
    elif i == 3:
        brd = three()
        N, M = M, N
        new_brd = []
    elif i == 4:
        brd = four()
        N, M = M, N
        new_brd = []
    elif i == 5:
        brd = five()
        new_brd = []
    else:
        brd = six()
        new_brd = []


for i in brd:
    print(*i)

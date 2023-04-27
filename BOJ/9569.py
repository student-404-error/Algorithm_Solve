# 돌게임이 너무 재미있다.

import sys
input = sys.stdin.readline
N = int(input())

win = [False]*(N+1)
win[1] = win[3] = win[4] = True

for i in range(5, N+1):
    if not win[i-1]:
        win.append(True)
    elif not win[i-3]:
        win.append(True)
    elif not win[i-4]:
        win.append(True)
    else:
        win.append(False)
if win[N]:
    print("SK")
else:
    print("CY")

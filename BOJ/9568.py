# 돌게임이 너무 재미있다.

import sys
input = sys.stdin.readline
N = int(input())

win = [False]*1001
win[2] = win[4] = True

for i in range(5, N+1):
    if not win[i-1]:
        win[i] = True
    elif not win[i-3]:
        win[i] = True
    elif not win[i-4]:
        win[i] = True

if win[N]:
    print("SK")
else:
    print("CY")
# print(win[1:N+1])

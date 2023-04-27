"""
v : 초기속력
m : 속력 변화 변수
t : 총 산책 시간
x, y : 현재 좌표
input
1 1 3

output
0 3
"""

import sys
input = sys.stdin.readline
v, m, t = map(int, input().split())
x = y = 0
for i in range(t):
    if i % 2 == 0:
        y += v
        v = (v*m)%10
    elif i % 2 == 1:
        x += v
        v = (v*m)%10
        v = v * (-1)
print(x, y)
import sys
input = sys.stdin.readline


def swap(x, y):
    ball[x], ball[y] = ball[y], ball[x]


ball = [1, 2, 3]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    x, y = ball.index(a), ball.index(b)
    swap(x, y)

print(ball[0])

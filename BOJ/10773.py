import sys
input = sys.stdin.readline

N = int(input())
K = []
for i in range(N):
    num = int(input())
    if num == 0:
        K.pop()
    else:
        K.append(num)

print(sum(K))
import sys

input = sys.stdin.readline

N = int(input())
ans = [[0] * N for i in range(N)]
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
ans[0][0] = arr[0][0]

for i in range(N - 1):
    for j in range(len(arr[i])):
        ans[i + 1][j] = max(ans[i][j] + arr[i + 1][j], ans[i + 1][j])
        ans[i + 1][j + 1] = ans[i][j] + arr[i + 1][j + 1]

print(max(ans[-1]))

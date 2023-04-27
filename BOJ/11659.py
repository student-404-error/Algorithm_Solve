import sys
input = sys.stdin.readline
N, M = map(int, input().split())
sum_list = list(map(int, input().split()))
sum_list.insert(0, 0)

for idx in range(N):
    sum_list[idx+1] = sum_list[idx+1] + sum_list[idx]

for i in range(M):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start-1])
# print(sum_list)
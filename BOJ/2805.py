# 나무 자르기
import sys
input = sys.stdin.readline
# 이진 탐색
# 매개 변수 탐색

# K: 1 <= K <= 10,000 가지고 있는 랜선의 갯수
# N: 1 <= K <= 1,000,000 필요한 랜선의 갯수
# 항상 K <= N
K, N = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)
mid = end

while start + 1 < end:
    mid = (start + end)//2
    n = 0
    for i in tree:
        if i > mid:
            n = n + i - mid
    if n >= N:
        start = mid
    else:
        end = mid
print(start)

# 평범한 배낭 문제
# from pprint import pprint
import sys
input = sys.stdin.readline
N, K = map(int,input().split()) # N은 아이템 갯수 K는 무게한도

item = [list(map(int, input().split())) for _ in range(N)]
# item[i][0] : 무게
# item[i][1] : 가치
V = [[0]*(K+1) for i in range(N+1)]
for i in range(1, N+1):
    for w in range(1, K+1):
        if item[i-1][0] <= w:
            V[i][w] = max(item[i-1][1] + V[i-1][w - item[i-1][0]], V[i-1][w])
        else:
            V[i][w] = V[i-1][w]
print(V[-1][-1])
# def knapsack(w :int, v: int) -> int:
#     """_summary_

#     Args:
#         w (int): weight limit
#         v (int): item value

#     Returns:
#         val: total value
#     """
#     if w > K:
#         return
#     if 
    
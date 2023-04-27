"""
미해결 이유 : 시간초과
"""
import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    a, b = map(int, input().split())
    A.append((a, b))
A.sort()

for i in A:
    print(i[0], i[1])

# for i in range(N):
#     for j in range(i, N):
#         if A[i][0] > A[j][0]:
#             A[i], A[j] = A[j], A[i]
#         elif A[i][0] == A[j][0]:
#             if A[i][1] > A[j][1]:
#                 A[i], A[j] = A[j], A[i]

# for i in A:
#     print(i[0], i[1])
import sys
input = sys.stdin.readline
N = int(input())
if N == 1:
    j = int(input())
    print(j)
    print(j)
    print(j)
    print(0)
    exit()
a = [int(input()) for _ in range(N)]


# A = []
# M ={}
# for i in range(N):
#     j = int(input())
#     if j not in A:
#         M.update({j:1})
#     else:
#         M.update({j:M.get(j)+1})
#     A.append(j)

# A.sort()
# most = max(M.values())
# most_dict = {}
# # 산술평균
# print(int(round(sum(A)/N, 0)))
# print(A[N//2])
# for i in M.keys():
#     if M[i] == most:
#         most_dict.update({i:M[i]})
# if len(most_dict) == 1:
#     print(most_dict.popitem()[0])
# else:
#     most_dict.pop(min(most_dict.keys()))
#     print(min(most_dict.keys()))
# print(A[-1]-A[0])

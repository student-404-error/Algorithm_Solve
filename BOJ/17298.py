# 오큰수 구하기
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

stack = []
# flag = True
result = [-1] * N
# ans = ''

for i in range(N):
    while stack and (A[i] > A[stack[-1]]):
        result[stack.pop()] = A[i]
    stack.append(i)

# while stack:
#     result[stack.pop()] = -1

print(*result)
        
#     su = A[i]
#     stack.append(su)
#     for j in range(i, N):
#         if A[j] > su:
#             result += str(A[j])+' '
#             flag = False
#             break
#     if flag:
#         result += str(-1) + ' '
#     flag = True
# print(result)


"""

만약 A[j] > A[i]라면 결과에 더한 후 continue
만약 A[j] <= A[i]라면 다음 stack에 넣을 수를 확인

"""
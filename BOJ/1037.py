import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# A.sort()
# print(A[0]*A[-1])
# 정렬 후 첫번째 값과 마지막 값을 곱하는 것은 리스트의 min, max를 곱하는 것과 같으므로
# 아래와 같이 작성할 수 있다.
print(max(A)*min(A))
# 정렬을 안해도 되므로 더 빠르다.
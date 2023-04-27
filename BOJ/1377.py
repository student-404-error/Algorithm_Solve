import sys
input = sys.stdin.readline
# print = sys.stdout.write
N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))
Max = 0
A.sort()

for i in range(len(A)):
    if Max < A[i][1] - i:
        Max = A[i][1] - i

print(Max+1)

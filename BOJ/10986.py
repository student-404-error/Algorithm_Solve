import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
C = [0]*M
cnt = 0
for i in range(1, len(A)): # 시작을 1로 해야함
    A[i] = A[i] + A[i-1]

"""
시작을 1로 하는 이유는 누적 합을 계산할 때, 첫 인덱스는 누적합을 계산하지 않아도 되기 때문이고,
아래 반복에서 시작을 0으로 하는 이유는 모든 누적 합 배열의 나머지를 구해야하기 때문이다.
"""
for i in range(0, len(A)): # 시작을 0으로 해야함
    remain = A[i] % M
    A[i] = remain
    if remain == 0:
        cnt+=1
    C[remain] += 1

C = [i for i in C if i != 0]

for j in C:
    cnt = cnt + ((j * (j-1))//2)
print(cnt)


"""
[1, 2, 3, 4]
1

3개의 수를 더해서 소수가 되는 순서쌍의 갯수

3 <= N <= 50
1 <= n <= 1000
"""

A = list(map(int, input().split()))
N = len(A)
chk = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            su = A[i] + A[j] + A[k]
            if su % 2 == 0:
                continue
            else:
                chk.append(su)
for i in chk:
    for j in range(3, i, 1):
        if i % j == 0:
            chk.remove(i)
            break
print(len(chk))
print(chk)
N = int(input())

A = list(map(int, input().split()))

# sosu = [True] * 1001
# 소수라면 TRUE
# 소수가 아니라면 FALSE
# sosu[0] =  sosu[1] = False

# m = int(round(1000**(1/2), 0))
# for i in range(2, m):
#     for j in range(i+i, 1000, i):
#         # print(i, j)
#         if sosu[j]:
#             sosu[j] = False

cnt = 0

for i in A:
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            break
    if j == i:
        cnt += 1

# for i in A:
#     if sosu[i]:
#         cnt += 1
print(cnt)
# N K => N의 약수 중 K번째로 작은 수
N, K = map(int,input().split())
cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
if cnt < K:
    print(0)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()


cnt = 0

for K in range(0, N):
    find = A[K]
    start_idx = 0
    end_idx = N-1
    while start_idx < end_idx:
        S = A[start_idx] + A[end_idx]
        if S == find:
            # print(find, A[start_idx], A[end_idx])
            if (end_idx != K) and (start_idx != K):
                # print(find, start_idx, end_idx)
                cnt+=1
                break
            elif start_idx == K:
                start_idx += 1
            elif end_idx == K:
                end_idx -= 1
        elif S > find:
            end_idx -= 1
        else:
            start_idx += 1
        
print(cnt)
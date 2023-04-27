import sys
input = sys.stdin.readline

N = int(input())

start_idx = end_idx = 1
cnt = 1
S = 1

while start_idx != N:
    if S == N:
        cnt += 1
        print('st_idx : ', start_idx, 'end_idx : ', end_idx, 'st+end : ', S)
        end_idx += 1
        S += end_idx
    elif S > N:
        S -= start_idx
        start_idx+=1
    else:
        end_idx+=1
        S += end_idx
    
print(start_idx)
print(cnt)
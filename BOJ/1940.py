import sys
input = sys.stdin.readline

N = int(input()) # 재료의 개수
M = int(input()) # 완성되야 하는 숫자

A = list(map(int, input().split()))
A.sort()

start_idx = 0
end_idx = N - 1
S = 0
cnt = 0

# 고유 번호라고 했으니 숫자가 중복되어 입력되는 일은 존재하지 않음.
# 그러므로 합이 M과 같을 때 양쪽의 인덱스를 모두 옮겨도 괜찮음.

while start_idx != end_idx:
    S = A[start_idx] + A[end_idx]
    if S == M:
        #print('st_idx : ', start_idx, 'end_idx : ', end_idx, 'st+end : ', S)
        cnt += 1
        end_idx -= 1
        start_idx += 1
    elif S < M:
        start_idx += 1
    else:
        end_idx -= 1
    
print(cnt)

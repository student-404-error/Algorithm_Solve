import sys
input = sys.stdin.readline
# print = sys.stdout.write

N = int(input()) # 숫자의 갯수 입력
A = [0] + [int(input()) for _ in range(N)]
# A는 숫자 리스트
tmp = [0] * int(N + 1)
# 병합하기 위한 리스트

def merge_sort(S, E):
    global A, tmp
    # 리스트의 길이가 1보다 작으면 재귀를 그만 돌아야함.
    if E - S < 1:
        return
    M = (S + E) // 2
    # 반을 나누기 위해 중간 인덱스 구하기
    merge_sort(S, M) # 0 2 -> 0 1 -> 0 0
    # 처음부터 중간까지 다시 분할
    merge_sort(M+1, E) # 3 5 -> 5 5
    # 중간+1부터 끝까지 분할
    for i in range(S, E+1):
        # print('m : ', M, 'now', A[i])
        # print('s, e : ', S, E)
        tmp[i] = A[i]
        print(tmp)
    k = S
    index1 = S
    index2 = M + 1
    while index1 <= M and index2 <= E:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= M:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= E:
        A[k] = tmp[index2]
        k += 1
        index2 += 1



    
    # print(A[S:E])

merge_sort(1, N)
# for i in range(1, N+1):
#     print(str(A[i])+'\n')
import sys
input = sys.stdin.readline
A, Q = map(int, input().split())
# A배열의 길이와 질문의 수 Q를 입력받는다.
B = sorted(map(int, input().split()))
B.insert(0, 0)
# 오름차순 정렬이 된 A 배열을 받는다.
# B_sum = [0]
# 누적합 리스트를 생성한다.
# for i in range(1, A+1):
#     B_sum.append(B[i] + B_sum[i-1])

# 변수를 새로 만들지 않고 해결
for i in range(1, A+1):
    B[i] = B[i] + B[i-1]

# Q회 만큼 반복하며 각 반복에서 답을 도출한 후 다음 반복으로 넘어감.
for i in range(Q):
    L, R = map(int, input().split())
    print(B[R] - B[L-1])



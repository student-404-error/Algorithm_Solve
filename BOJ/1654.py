# 랜선 자르기
import sys
input = sys.stdin.readline
# 이진 탐색
# 매개 변수 탐색


def check(l: int):  # l: 랜선의 길이
    n = 0  # 만들 수 있는 총 랜선 갯수


# K: 1 <= K <= 10,000 가지고 있는 랜선의 갯수
# N: 1 <= K <= 1,000,000 필요한 랜선의 갯수
# 항상 K <= N
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
if N == 1:
    print(max(lan))
    exit()
# 0 ~ max(lan)까지 이진 탐색
start, end = 0, max(lan)+1
mid = end

while start+1 < end:
    mid = (start + end)//2
    n = 0
    for i in lan:
        n = n + i//mid
    if n >= N:
        start = mid
    else:
        end = mid
print(start)


"""
** step 1 **
- start = 0
- now = 0
- mid = 401
(now + end) // 2 ==> 401 False;
- end = 802

- n = 7
==> False; binary_search(start, end, mid) ## 0, 802, 401

** step 2 **
- start = 0
- now = 802
(now + end) // 2 ==> 600 False;
- mid = 200

- end = 401

- n = 11
==> True; binary_search(mid, start, end) ## 200, 0, 401

"""

"""
N개의 수 A1, A2, ..., AN과 L이 주어진다.

Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

1. A[i-L+1] ~ A[i] 사이의 수 최솟값을 미리 하나 지정해둔다.
2. 범위가 바뀔 때, 오른 쪽으로 한칸 늘어나고 왼쪽에서 한칸 줄어든다.
3. 범위가 변경될 때마다 최솟값과 비교해 작다면 바꾼다.
4. 정렬은 하면 안됨
5. 초기값은 A[0]로 설정


-- 변수 정리 --
N : 수의 갯수 
L : 범위
A : 숫자들의 리스트
min_num : 최솟값을 저장해둘 배열
result : 결과값을 하나씩 담아둘 배열

-- 규칙 --
1. L이 3이므로 i - L + 1은 i가 2일 때까지 음수이다. 
2. 그러므로 i가 L-1일 때까지 추가만 하면 된다. 음수는 무시해야하기에.
"""

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
min_num = A[0]
result = []
end_idx = 0

def add_num(x):
    global min_num
    if x < min_num:
        print('min_range : ', A[i:j])
        min_num = x

def remove_num(x, i, j):
    global min_num, A
    
    if x == min_num:
        print('min_range : ', A[i:j])
        min_num = min(A[i:j])

for i in range(L-1): # 0 1
    add_num(A[i])
    result.append(min_num)

for i in range(0, N-L+1): # 0 1 2 3 4 5 6 7 8 총 9번 
    j = i + L - 1
    result.append(min_num)
    print(j)
    remove_num(A[i], i+1, j+2)
    add_num(A[j])
    
    

print(result)
# 숫자카드 2
import sys
input = sys.stdin.readline

# Set은 중복을 허용하지 않음. 집합.
# Map은 Dictionary와 동일함.
# key, value를 갖는 자료구조
# Hash를 이용한 풀이를 하기 위해서
# 상근이 카드를 배열에 Hashing함.

N = int(input())  # 상근이가 가지고 있는 카드 수
have = list(map(int, input().split()))  # 상근이 카드
M = int(input())  # 찾을 카드 수
find = list(map(int, input().split()))  # 갯수를 찾을 카드
min_have, max_have = min(have), max(have)

hashing = [0 for _ in range(20000001)]  # max - min + 1
for i in have:
    hashing[i+abs(min_have)] += 1

for i in find:
    print(hashing[i+abs(min_have)], end=" ")

# N 은 테스트 케이스 수
"""
6 12 10 -> 402
30 50 72  -> 1203
"""
import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    H, W, N = map(int, input().split())  # ex 5 9 15
    # H - 건물의 높이 (층수)
    # W - 건물의 넓이 (호수)
    # N - 몇번째로 찾아온 손님인지

    ho = N // H  # 3
    # 층수 관계없이 1호가 가장 먼저 채워지므로
    # 현재 채워져 있는 방을 알고
    # 들어갈 방의 호수를 구하기 위해

    floor = N % H  # = 0
    # 호수를 구했으니 층수를 구해야할 차례
    # 층수는 0~H-1층까지 계산결과가 나옴

    if floor == 0:  # 층수가 0이라면
        floor = H  # 나누어 떨어진 것이므로 꼭대기 층
    elif floor >= 1:  # 층이 0이 아니라면
        ho += 1      # 다음 호수에 거주해야함.
    if ho <= 9:  # 출력형식
        print(f'{floor}0{ho}')
    else:
        print(f'{floor}{ho}')

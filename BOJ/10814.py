# 나이순 정렬
import sys
input = sys.stdin.readline

n = int(input())  # 정렬할 데이터 갯수
name = []  # 이름과 나이를 담을 리스트
for i in range(n):
    age, na = input().split()
    name.append([int(age), na])  # 나이는 int로 변환 후 리스트에 추가 -> sort를 편하게 하기 위해
    # age가 문자열이라면 "10"이 "9"보다 우선임. 문자열은 한자리씩 비교하기 때문.
dic = sorted(name, key=lambda x: x[0])  # lambda식을 사용하여 키 설정 후 키를 기준으로 정렬

for i in dic:
    print(i[0], i[1])

# 그룹 단어 체커
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    word = input().rsplit()[0]
    isGroupWord = True          # 그룹단어인지 확인하기 위한 변수
    checker = []                # 각 단어별로 이미 나온 단어인지 확인하기 위한 리스트
    pre = ''                    # 바로 직전에 나왔던 문자를 담아놓을 변수
    for i in word:
        if i not in checker:    # i가 checker list에 없으면
            checker.append(i)   # checker에 추가 후
            pre = i             # pre를 i로 초기화
        else:                   # i가 checker list에 있으면
            if i != pre:        # 하지만 pre와 i가 같지 않으면 --> 떨어져서 나온 문자이므로 그룹단어 X
                isGroupWord = False
                break
    if isGroupWord:
        cnt += 1
print(cnt)

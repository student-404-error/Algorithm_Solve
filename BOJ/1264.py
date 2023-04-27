# import sys
# input = sys.stdin.readline

chk = ['a', 'e', 'u', 'o', 'i']
cnt = 0
while True:
    A = str(input()).lower()
    if A == "#":
        break
    for i in A:
        if i in chk:
            cnt += 1
    print(cnt)
    cnt = 0


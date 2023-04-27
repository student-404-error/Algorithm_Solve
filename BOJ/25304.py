# 영수증
total = int(input())

N = int(input())
s = 0
for i in range(N):
    val, cnt = map(int, input().split())
    s = s + (val*cnt)
if s == total:
    print("Yes")
else:
    print("No")
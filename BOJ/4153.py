import sys
input = sys.stdin.readline


while True:
    tr = list(map(int, input().split()))
    if sum(tr) == 0:
        break
    c = max(tr)
    tr.remove(c)
    tr = list(map(lambda x : x**2, tr))
    if sum(tr) == c**2:
        print("right")
    else:
        print("wrong")
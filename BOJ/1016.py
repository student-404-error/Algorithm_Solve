from math import sqrt
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dec = [True] * (m + 1 - n)

ms = int(sqrt(m))
power = []
isPower = [True] * (ms-1)

for i in range(2, ms+1, 1):
    power.append(i*i)
for i in range(len(isPower)):
    # print("i ->", i)
    if isPower[i]:
        for j in range(i+i+2, ms-1, i+2):
            # print("j ->", j)
            if isPower[j]:
                isPower[j] = False
                power[j] = 0
            # print("i ->", i)
            # print("j ->", j)
            # print("isPower ->", isPower)
            # print("------------------------")

    # for j in range(i*i, m+1, i*i):
    #     if n <= j <= m:
    #         dec[j - n] = False
for i in range(ms-1):
    # print(power[i])
    if isPower[i]:  # power[i]가 0이 아니면, isPower[i]가 True면
        j = n
        while j <= m:
            # print("j1 ==>> ", j)
            # print("T/F >> ", dec[j - n])
            # if not dec[j - n]:
            #     j += power[i]
            if dec[j - n]:
                if j % power[i] == 0:
                    dec[j - n] = False
                    j += power[i]
                    # if not dec[j - n]:
                    #     j += power[i]
                    #     print("j2 ==>> ", j)
                else:
                    j += 1
            else:
                j += 1

print(dec.count(True))
# print(dec)

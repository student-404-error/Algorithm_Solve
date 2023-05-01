import sys
import time
input = sys.stdin.readline

n, m = map(int, input().split())
start = time.time()
dec = [True] * (m + 1 - n)

ms = int(m**(1/2))
power = []
isPower = [True] * (ms-1)

for i in range(2, ms+1, 1):
    power.append(i*i)
for i in range(ms-1):
    if isPower[i]:
        for j in range(i+i+2, ms-1, i+2):
            if isPower[j]:
                isPower[j] = False
for i in range(ms-1):
    if isPower[i]:  # power[i]가 0이 아니면, isPower[i]가 True면
        j = n
        while j <= m:
            if dec[j - n]:
                if j % power[i] == 0:
                    dec[j - n] = False
                    j += power[i]
                else:
                    j += 1
            else:
                j += 1

print(dec.count(True))
print("time : ", time.time() - start)

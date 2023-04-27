A = [False]*31
for i in range(28):
    a = int(input())
    A[a] = True

for i in range(1, 31):
    if not A[i]:
        print(i)

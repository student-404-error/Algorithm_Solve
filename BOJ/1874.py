N = int(input())
stack = []
A = []
result = []
flag = True
idx = 0
for i in range(N):
    A.append(int(input()))

num = 1
j = 0

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            result.append('+')
        stack.pop()
        result.append('-')
        idx += 1
    else:
        n = stack.pop()
        if su < n:
            print('NO')
            flag = False
            break
        else:
            result.append('-')

if flag == True:
    for i in result:
        print(i)

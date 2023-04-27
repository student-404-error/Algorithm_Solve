N = int(input())
A = []

for i in range(N):
    A.append(int(input()))
change = False
for i in range(0, N-1):
    for j in range(0, N-i-1):
        if A[j] > A[j+1]:
            A[j+1], A[j] = A[j], A[j+1]
            change = True
    if change == False:
        print(i)
        break
    
# for i in A:
#     print(i)
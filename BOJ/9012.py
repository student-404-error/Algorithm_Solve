import sys
input = sys.stdin.readline

N = int(input())


for i in range(N):
    A = str(input())
    stack = []
    for j in range(0, len(A)-1):
        if stack == []:
            stack.append(A[j])
        elif A[j] == "(":
            stack.append(A[j])
        elif (stack[-1] == "(") and (A[j] == ")"):
            # 스택이 다 비어버리면 -1인덱스를 찾을 수 없으므로 조건으로 하나 더 붙여줘야할 듯
            stack.pop()
        else:
            stack.append(A[j])
    if stack:
        print("NO")
    else:
        print("YES")

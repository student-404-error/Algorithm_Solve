import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
A = [2, 3, 5, 7]
N = int(input())

def sosu(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10, 2):
            n = num * 10 + i
            if sosu(n):
                DFS(n)

for i in A:
    DFS(i)


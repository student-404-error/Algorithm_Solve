n = int(input())
arr = [1, 1, 1, 2, 2]

v = [int(input()) for i in range(n)]
for i in range(0, max(v)):
    arr.append(arr[i] + arr[i + 4])
for i in v:
    print(arr[i - 1])

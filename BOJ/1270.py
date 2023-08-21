import sys

input = sys.stdin.readline


def candidateSelect(arr: list):
    cand = arr[1]
    cnt = 0
    for i in range(2, arr[0] + 1):
        if cand == arr[i]:  # if cand equal arr[i], then cnt += 1
            cnt += 1
        elif cnt == 0:
            cand = arr[i]
        else:  # cnt is not zero and appear another number
            cnt -= 1
    return cand


def checkCandidate(arr: list, cand: int) -> str:
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] == cand:
            cnt += 1

    if cnt > (arr[0] // 2):
        return str(cand)
    else:
        return "SYJKGW"


N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    cand = candidateSelect(arr)
    print(checkCandidate(arr, cand))

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

# def quick_sort(S, E, K):
#     global A

#     if S < E:
#         pivot = partition(S, E)
#         if pivot == K:
#             return
#         elif K < pivot:
#             quick_sort(S, pivot-1, K)
#         else:
#             quick_sort(pivot, E, K)

# def swap(i, j):
#     global A
#     A[i], A[j] = A[j], A[i]

# def partition(S, E):
#     global A
#     if S+1 == E:
#         if A[S] > A[E]:
#             swap(S, E)
#         return E
#     M = (S+E)//2
#     swap(S, M)
#     pivot = A[S]
#     i = S + 1
#     j = E
#     while i <= j:
#         while pivot < A[j] and j > 0:
#             j = j - 1
#         while pivot > A[i] and i < len(A) - 1:
#             i = i + 1
#         if i <= j:
#             swap(i, j)
#             i = i + 1
#             j = j - 1
#     A[S] = A[j]
#     A[j] = pivot
#     return j

# quick_sort(0, N - 1, K - 1)
# print(A[K-1])
# def pivot(start, end):
#     global A

# A = [5,3,8,4,9,1,6,2,7]

def quick_sort(start, end, K):
    global A
    if start >= end:
        # print('why end?', start, end)
        return 1
    pivot = A[start]
    # print('----------------')
    # print('pivot', pivot)
    i = start + 1
    j = end
    while i<=j:
        # print('A : ', A)
        # print('i, j', A[i], A[j])
        if A[i] <= pivot:
            i += 1
        elif A[j] >= pivot:
            j -= 1
        elif A[j] < A[i]:
            A[i], A[j] = A[j], A[i]
            # swap(A[i], A[j])
        # print('A : ', A)
        # print('i, j', A[i], A[j])
    A[j], A[start] = A[start], A[j]
    # print('s, j, e, p: ',start, j, end, pivot)
    # print('----------------')
    if K == j:
        print(A[j])
        sys.exit()
    quick_sort(start, j, K)
    quick_sort(i, end, K)
    # quick_sort(i, )
    return 0
quick_sort(0, N-1, K-1)

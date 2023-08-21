import itertools as it

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in sorted(it.permutations(a, m)):
    print(*i)

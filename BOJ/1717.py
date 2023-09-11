# 집합의 표현 (유니온파인드)
# Gold 5
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s = [_ for _ in range(0, n + 1)]


def union(a: int, b: int):
    x = find(a)
    y = find(b)
    if x is not y:
        s[y] = x
    # print(s)


def find(a: int) -> int:
    """Not Recursion

    Args:
        a (int): target number

    Returns:
        int: a's root node
    """
    # print("before : ", a)
    while s[a] != a:
        a = s[a]
    # print("after : ", s[a])
    return s[a]


def check(a: int, b: int):
    x = find(a)
    y = find(b)
    if x == y:
        return "YES"
    else:
        return "NO"


def answer():
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd:  # find
            print(check(a, b))
        else:  # union
            union(a, b)


answer()

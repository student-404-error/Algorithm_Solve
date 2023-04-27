# 별찍기 15
n = int(input())
j = -1
for i in range(n, 0, -1):
    print(" "*(i-1), end="*")
    if i != n:
        print(" "*j, end="*")
    j += 2
    print("")

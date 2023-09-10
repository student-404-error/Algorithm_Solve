a, b = map(int, input().split())
if a > b:
    b, a = a, b

# if a == b:
#     print(0)
# else:
#     print(b - a - 1)


# if a + 1 == b:
#     print(0)
# else:
#     for i in range(a + 1, b - 1):
#         print(i, end=" ")
#     print(b - 1)
def answer(a, b):
    cnt = 0
    num = []
    if a == b:
        print(0)
        return
    elif a + 1 == b:
        print(0)
        return
    else:
        print(b - a - 1)
        for i in range(a + 1, b):
            num.append(i)
        print(*num)


answer(a, b)

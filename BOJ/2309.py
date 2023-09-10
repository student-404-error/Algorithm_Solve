# 일곱 난쟁이 -> B1
# 그리디인 것 같음
# 근데 생각해보면 그리디가 안됨

a = [int(input()) for i in range(9)]
s = sum(a)

# a.remove(15)
# a.remove()
# print(a)


def answer():
    for i in range(0, 8, 1):  # 0 ~ 7까지
        for j in range(i + 1, 9, 1):  # 7, 8
            if s - a[i] - a[j] == 100:
                # print(a[i], a[j])
                rm = a[j]
                a.remove(a[i])
                a.remove(rm)
                a.sort()
                return 0


def pr():
    for i in a:
        print(i)


answer()
pr()

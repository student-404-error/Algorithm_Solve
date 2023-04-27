def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        print(x, n)
        return power(x*x, n//2)
    elif n % 2 != 0:
        print(x, n)
        return x * power(x*x, (n-1)//2)
print(power(3, 2))
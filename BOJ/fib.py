def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(5))
# n번째에 있는 피보나치 수열을 출력

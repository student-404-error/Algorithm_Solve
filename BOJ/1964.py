n = int(input())

dp = 5

for i in range(2, n+1):
    dp = (dp+((i*3)+1))
print(dp % 45678)

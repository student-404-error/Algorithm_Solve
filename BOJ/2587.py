# 대표값2 => bronze2
# 평균과 중앙값을 출력

# 무조건 5개 숫자 입력
a = [int(input()) for _ in range(5)]
a.sort()
print(f"{sum(a)//len(a)}\n{a[len(a)//2]}")

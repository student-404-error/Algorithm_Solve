# 너의 평점은
subject = [list(map(str, input().split())) for _ in range(20)]
s = 0
score = cnt = 0

for i in subject:
    if i[2] == 'P':
        continue
    s += float(i[1])
    cnt += 1
    if i[2] == 'A+':
        score += float(i[1]) * 4.5
    elif i[2] == 'A0':
        score += float(i[1]) * 4.0
    elif i[2] == 'B+':
        score += float(i[1]) * 3.5
    elif i[2] == 'B0':
        score += float(i[1]) * 3.0
    elif i[2] == 'C+':
        score += float(i[1]) * 2.5
    elif i[2] == 'C0':
        score += float(i[1]) * 2.0
    elif i[2] == 'D+':
        score += float(i[1]) * 1.5
    elif i[2] == 'D0':
        score += float(i[1]) * 1.0
print(f'{score/s:.6f}')

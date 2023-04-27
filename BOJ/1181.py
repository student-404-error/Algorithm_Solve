from sys import stdin
input = stdin.readline

n = int(input())
word = []
for _ in range(n):
    w = input().strip()
    l = len(w)
    if (w, l) not in word:
        word.append((w, l))
word = sorted(word, key=lambda x: (x[1], x[0]))

for i in word:
    print(i[0])

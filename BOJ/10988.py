import sys
input = sys.stdin.readline
palindrome = input().split()[0]
# remove = ['.', ',', '\'', '"', ' ']
stack = []
isPalin = True

# for i in remove:
#     palindrome = palindrome.replace(i, '')

# print(palindrome[0])
s = len(palindrome)
for i in range(s//2):
    stack.append(palindrome[i])

if s % 2 == 0:
    for j in range(s//2, s, 1):
        if stack[-1] != palindrome[j]:
            isPalin = False
            break
        stack.pop()
else:
    for j in range((s//2)+1, s, 1):
        if stack[-1] != palindrome[j]:
            isPalin = False
            break
        stack.pop()

if isPalin:
    print('1')
else:
    print('0')

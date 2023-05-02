# 크로아티아 알파벳
import sys
input = sys.stdin.readline

syn = input().split()[0]
cnt = 0
calpha = ['c=', 'c-', 'dz=', 'd-', 's=', 'z=', 'lj', 'nj']

for i in calpha:
    cnt += syn.count(i)
print(len(syn)-cnt)
i = 0
# while i < len(syn):
#     if len(syn) == 1:
#         cnt = 1
#         break
#     if syn[i] == 'c':
#         if syn[i+1] == '-' or syn[i+1] == '=':
#             cnt += 1
#             i += 1
#         else:
#             cnt += 1
#     elif syn[i] == 'd':
#         if syn[i+1] == '-':
#             cnt += 1
#             i += 1
#         elif syn[i+1:i+3] == 'z=':
#             cnt += 1
#             i += 2
#         else:
#             cnt += 1
#     elif syn[i] == 'l' or syn[i] == 'n':
#         if syn[i+1] == 'j':
#             cnt += 1
#             i += 1
#         else:
#             cnt += 1
#     elif syn[i] == 's' or syn[i] == 'z':
#         if syn[i+1] == '=':
#             cnt += 1
#             i += 1
#         else:
#             cnt += 1
#     else:
#         cnt += 1
#     i += 1
#     if i == len(syn)-1:
#         cnt += 1
#         break
# print(cnt)

# break 테스트

# for i in range(10):
#     print(i)
#     for j in range(5):
#         print(j)
#         if j == 3:
#             break
#     print(i)

import sys
input = sys.stdin.readline

n = int(input())
if n % 2 == 0:
    print("CY")
else:
    print("SK")

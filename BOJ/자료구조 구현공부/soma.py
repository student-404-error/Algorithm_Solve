# [1,4] [3, 4] [1, 10]
from itertools import combinations
from collections import Counter

a = [[1, 4], [3, 4], [1, 10]]
b = Counter(a)
# b = []
# for i in a:
#     for j in range(2):
#         if i[j] not in b:
#             b.append(i[j])
# b = list(combinations(b, 2))
# # c = [i for i in b if i not in a]
# print(b)
print(a)
        # for i in range(2):
#     for j in range(2):
#         if a[i][j] in a[i+1]:
#             break
#         if j == 1:

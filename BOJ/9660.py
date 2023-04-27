# stone Game 7
"""
1  2   3   4   5   6   7
1  2   3   4   5   6   7
SK CY  SK  SK  SK  SK  CY

8  9   10  11  12  13  14
SK CY  SK  SK  SK  SK  CY

Repeat cycles based on 7
"""
import sys
input = sys.stdin.readline

game = [False, True, False, True, True, True, True]  # cycle
# 7n % 7 = 0 so cycle=[7, 1, 2, 3, 4, 5, 6]
n = int(input())
if game[n % 7]:
    print('SK')
else:
    print('CY')

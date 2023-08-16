# https://www.acmicpc.net/problem/10775
# 10775 공항
# Memory: 35108 KB, Time: 144 ms, python3

"""

"""""

import sys; readline = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

ans = 0
for _ in range(int(readline())):
    a, b, c = readline().split()
    a, c = int(a), int(c)
    if b == '+':
        ans += a + c
    elif b == '-':
        ans += a - c
    elif b == '*':
        ans += a * c
    elif b == '/':
        ans += a // c

print(ans)
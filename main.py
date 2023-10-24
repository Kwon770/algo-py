"""
https://www.acmicpc.net/problem/10775
10775 공항
Memory: 35108 KB, Time: 144 ms, python3
"""""

import sys; readline = sys.stdin.readline

N, K = map(int, readline().split())
things = [(0,0)]
for _ in range(N):
    W, V = map(int, readline().split())
    things.append((W, V))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for n in range(1, N + 1):
    w, v = things[n]

    for k in range(1, K + 1):
        if k < w:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - w] + v)

print(dp[N][K])
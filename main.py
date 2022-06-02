# https://www.acmicpc.net/problem/13227
# 13227 Tic Tae Toe
# Memory : 30840 KB / Time : 68 ms

import sys; readline = sys.stdin.readline

pattern = [
    ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
    ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
    ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))]

def solve():
    for i in range(len(pattern)):
        p = pattern[i]
        if b[p[0][0]][p[0][1]] != '.' and b[p[0][0]][p[0][1]] == b[p[1][0]][p[1][1]] == b[p[2][0]][p[2][1]]:
            print("YES")
            return

    print("NO")

b = []
for _ in range(3):
    b.append(input())

solve()
# https://www.acmicpc.net/problem/1477
# 1477 휴게소 세우기
# Memory: 32156 KB, Time: 44 ms


"""
"""""

import sys; readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

V, E = map(int, readline().split())
edges = []
parents = [i for i in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, readline().split())
    edges.append((C, A, B))
edges.sort()

def find(x):
    global parents

    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    global parents

    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

ans = 0
for C, A, B in edges:
    if find(A) == find(B):
        continue

    union(A, B)
    ans += C
print(ans)

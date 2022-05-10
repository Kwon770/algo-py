# https://www.acmicpc.net/problem/2583
# 2583 영역 구하기
# Memory : 32412 KB / Time : 104 ms

import sys; readline = sys.stdin.readline

for _ in range(int(readline())):
    n = int(readline())
    a = list(map(int, readline().split()))

    a.sort()
    if a[0] == 0:
        zeros = 0
        for ele in a:
            if ele != 0:
                break
            zeros += 1

        print(n - zeros)

    else:
        duplicated = False
        for i in range(1, len(a)):
            if a[i - 1] == a[i]:
                duplicated = True
                break

        if duplicated:
            print(n - 1 + 1)
        else:
            print(n - 1 + 2)
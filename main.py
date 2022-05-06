# https://www.acmicpc.net/problem/2583
# 2583 영역 구하기
# Memory : 32412 KB / Time : 104 ms

import sys; readline = sys.stdin.readline

for _ in range(int(readline())):
    s = input()

    if len(s) == 1:
        print(1)
        continue

    non_one = True
    non_zero = True
    last_one = 0
    first_zero = 0

    for i in range(len(s)):
        if s[i] == '1':
            non_one = False
            last_one = i
        elif s[i] == '0':
            if non_zero:
                first_zero = i

            non_zero = False

    if not non_one and not non_zero:
        print(first_zero - last_one + 1)

    elif non_one and not non_zero:
        if first_zero == 0:
            print(1)
        else:
            print(first_zero + 1)

    elif not non_one and non_zero:
        if last_one == len(s) - 1:
            print(1)
        else:
            print(len(s) - last_one)

    else:
        print(len(s))
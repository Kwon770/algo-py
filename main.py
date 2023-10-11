# https://www.acmicpc.net/problem/10775
# 10775 공항
# Memory: 35108 KB, Time: 144 ms, python3

"""

"""""
import sys; readline = sys.stdin.readline
INF = 9876543210

def get_t_price(type, price):
    if type == "Mugunghwa" or type == "ITX-Saemaeul" or type == "ITX-Cheongchun":
        return 0
    elif type == "S-Train" or type == "V-Train":
        return price / 2
    else:
        return price


N, R = map(int, readline().split())
cities = list(set(readline().split()))
C = len(cities)
city_idx = dict()
for i in range(C):
    city_idx[cities[i]] = i

M = int(readline())
path = list(readline().split())
K = int(readline())

prices = [[INF for _ in range(C)] for _ in range(C)]
t_prices = [[INF for _ in range(C)] for _ in range(C)]
for _ in range(K):
    typei, a, b, price = readline().split()
    a = city_idx[a]
    b = city_idx[b]
    price = int(price)

    prices[a][b] = min(prices[a][b], price)
    prices[b][a] = min(prices[b][a], price)
    t_prices[a][b] = min(t_prices[a][b], get_t_price(typei, price))
    t_prices[b][a] = min(t_prices[b][a], get_t_price(typei, price))


for mid in range(C):
    for start in range(C):
        for end in range(C):
            prices[start][end] = min(prices[start][end], prices[start][mid] + prices[mid][end])
            t_prices[start][end] = min(t_prices[start][end], t_prices[start][mid] + t_prices[mid][end])

total_price = 0
t_total_price = R
for i in range(M - 1):
    start = city_idx[path[i]]
    end = city_idx[path[i + 1]]

    total_price += prices[start][end]
    t_total_price += t_prices[start][end]


if total_price > t_total_price:
    print("Yes")
else:
    print("No")
from collections import deque
import heapq

INF = int(1e9)

def dfs(graph, v, visited):
    # graph, a에서 갈 수 있는 인접 노드들, 인접 행렬
    visitied[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(n):
    # graph, a에서 갈 수 있는 인접 노드들, 인접 행렬
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

def dijkstra(start):
    # graph, a에서 갈 수 있는 인접 노드들, 인접 행렬
    distance = [INF] * (n+1)

    q = [(start, 0)]
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = distance[now] + node[1]
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, (node[0], cost))


def floyd():
    # graph, a to b의 가중치, 2d arr
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


def bellman(start):
    # edges, (a, b, val), 1d arr
    for i in range(v):
        for j in range(e):
            a, b, c = edges[j]

            if distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == v - 1:
                    return False # 사이클
    return True
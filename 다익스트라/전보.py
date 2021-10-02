# import sys

# inf = int(1e9)

# n, m, c = list(map(int, sys.stdin.readline().split()))
# graph = [[inf] * (n + 1) for i in range(n + 1)]

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# for i in range(m):
#     x, y, z = list(map(int, sys.stdin.readline().split()))
#     graph[x][y] = z
#     graph[y][x] = z

# for i in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# cnt = 0
# max_value = 0
# for i in range(1, n + 1):
#     if graph[c][i] != inf:
#         cnt += 1
#         max_value = max(max_value, graph[c][i])
    
# print(cnt - 1, max_value)

import sys
import heapq

inf = int(1e9)

n, m, start = list(map(int, sys.stdin.readline().split()))
graph = [[] for i in range(n + 1)]
distance = [inf] * (n + 1)

for i in range(m):
    x, y, z = list(map(int, sys.stdin.readline().split()))
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

cnt = 0
max_distance = 0
for i in distance:
    if i != inf:
        cnt += 1
        max_distance = max(max_distance, i)

print(cnt - 1, max_distance)
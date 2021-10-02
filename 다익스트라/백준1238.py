import sys
import heapq

inf = int(1e9)

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
distance = [inf] * (n + 1)
graph_r = [[] for i in range(n + 1)]
distance_r = [inf] * (n + 1)

def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph_r[b].append([a, c])

dijkstra(x, distance, graph)
dijkstra(x, distance_r, graph_r)
max_ = 0
for i in range(1, n + 1):
    max_ = max(max_, distance[i] + distance_r[i])

print(max_)

 
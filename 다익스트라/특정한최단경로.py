'''
백준 1504

방향성이 없고, 1번 정점에서 n번 정점으로 최단거리로 이동하는데, 특정 정점 v1, v2를 지나야 한다.
그래서 1번에서 시작해서 v1, v2를 지나 n번으로 도착하는 최단거리를 구하면 된다.

'''

import heapq
import sys

inf = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [inf] * (n + 1)
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

    return distance

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n] # 1에서 v1까지 가는 촤단거리 + v1에서 v2까지 가는 최단 거리 + v2에서 n까지 가는 최단거리
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n] # 1에서 v2까지 가는 최단거리 + v2에서 v1까지 가는 최단 거리 + v1에서 n까지 가는 최단거리

result = min(v1_path, v2_path)

print(result if result < inf else -1)




    


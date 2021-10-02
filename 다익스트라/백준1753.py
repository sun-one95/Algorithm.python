import heapq
import sys

inf = int(1e9)

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)] 
distance = [inf] * (n + 1) # 최단거리를 기록해줄 리스트 설정 초기값은 inf

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c)) # a에서 b 까지의 거리가 c라는 의미

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

for i in range(1, n + 1):
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])
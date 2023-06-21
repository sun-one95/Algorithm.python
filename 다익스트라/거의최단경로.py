'''
백준 5719

다익스트라 알고리즘을 사용해 최단 경로를 얻어내고, BFS를 통해 최단 경로에 사용된 간선을 제거할 수 있다.
이후 다익스트라 알고리즘을 사용하면서 (이때 이전의 간선은 사용할 수 없다) 거의 최단경로를 얻는다.

1. 최단 경로를 구하기 위해 다익스트라 알고리즘을 사용하자.
2. 최단 경로에 사용된 간선을 확인하기 위해 BFS를 사용해 접근하자
3. 조건은 목적지에서 거꾸로 출발지로 향하면서 인접 노드에서 여기까지 오는 비용이 최단경로 distance
에 기록된 비용과 일치한다면 곧 최단경로를 얻는데 사용한 노드라는 점이다.
4. 다시 한 번 다익스트라 알고리즘으로 거의 최단 경로 찾는다. 목적지까지 거리가 무한이라면 찾을 수 없다는 뜻
'''

from heapq import heappush, heappop
from collections import deque   
import sys

INF = int(1e9)
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())
    graph = [[] for _ in range(n)]
    graph_inv = [[] for _ in range(n)]
    edges = [[False for _ in range(n)] for _ in range(n)]

    for i in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        graph_inv[v].append((u, p))

    def dijkstra(start):
        distance = [INF] * n
        distance[start] = 0
        q = []
        heappush(q, (0, start))

        while q:
            dist, now = heappop(q)
            if distance[now] < dist:
                continue

            for i in graph[now]:
                if edges[now][i[0]]: continue
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heappush(q, (cost, i[0]))

        return distance

    

    def bfs():
        q = deque()
        q.append(d)

        while q:
            now = q.popleft()

            if now == s: continue

            for i in graph_inv[now]:
                if distance[i[0]] + i[1] == distance[now] and not edges[i[0]][now]:
                    edges[i[0]][now] = True
                    q.append(i[0])

    distance = dijkstra(s)
    bfs()
    distance = dijkstra(s)

    if distance[d] == INF: print(-1)
    else: print(distance[d])
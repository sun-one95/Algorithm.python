'''
백준 9370

시작점에서 출발하여 g, h를 지났다는 단서를 고려하여 x1, x2 등에 도달했는지 판단하는 문제다.

그러므로 시작점, g, h 간의 최단거리를 다익스트라 알고리즘을 통해 구한 다음

시작점(g) + g(h) + h(x1) = 시작점(x1) 이거나 시작점(h) + h(g) + g(x1) = 시작점(x1) 이럴때 답이된다.

왜냐면 어쨌든 x1, x2가 도착지 후보이므로

시작점에서 도착지로 가는 최단거리와 위에 구한 거리가 같아야 하므로(최단거리로 구했다고 문제에 적힘)

위와 같이 풀이를 진행한다.
'''

from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance
    
for tc in range(int(input())):
    n, m, t = map(int, input().split())
    start, g, h = map(int, input().split())

    graph = [[] for i in range(n + 1)]
    de = []
    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for i in range(t):
        de.append(int(input()))

    start_dist = dijkstra(start)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)
    answer = []
    for x in de:
        if start_dist[g] + g_dist[h] + h_dist[x] == start_dist[x] or start_dist[h] + h_dist[g] + g_dist[x] == start_dist[x]:
            answer.append(x)
    
    answer.sort()
    for i in answer:
        print(i, end=' ')
    print()
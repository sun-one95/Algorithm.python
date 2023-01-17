'''
백준 11779

기존 다익스트라 알고리즘으로 이 문제를 푼다.
추가적으로 문제에서 요구하는 게, 시작점에서 끝점까지의 최단거리에서 거친 노드들을 찾아서 그들의 개수와 무엇인지 나열해야 한다.

어려웠던 점
어떤 느낌인지 알아서 풀기 쉽겠구나 했는데 최단거리를 거친 노드들을 담을려고 하는데 어려움이 있었다.

해결
각 노드들의 이전 노드들을 저장하는 리스트를 만들고 각 노드들에 대한 최단거리를 갱신할때 마다 그 노드의 이전 노드를 아까 우선순위 큐에서 추출한 노드로 초기화한다.
그러면 문제를 해결할 수 있다.
'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
prev_node = [0] * (n + 1) # 자기 이전의 노드 담는 리스트

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

x, y = map(int, input().split())

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
                prev_node[i[0]] = now
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)
print(distance[y])

path = [y]
now = y
while now != x:
    now = prev_node[now]
    path.append(now)

path.reverse()
print(len(path))
for i in path:
    print(i, end=' ')
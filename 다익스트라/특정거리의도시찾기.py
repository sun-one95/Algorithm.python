'''
백준 18352

다익스트라 알고리즘을 이용해서 x의 관한 최단거리 리스틀 구한다.
그래서 최단거리 중에서 k이랑 같은 값의 최단거리를 가지는 정점을 출력한다.
만약 없다면 -1을 출력한다.

여기서 막혔던 점은 마지막에 거리 k와 같은 최단거리인 노드를 출력했느데, 없을 때는 -1리턴이 
안되서 난감했다. 그냥 쉽게 새로 리스트를 만들어서 최단거리가 k인 노드들을 그 리스트에 넣고 만약 그 리스트가 비어있다면 -1이고
아니라면 차례대로 노드를 출력하면 된다.
'''

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

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

    
dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i, end='\n')

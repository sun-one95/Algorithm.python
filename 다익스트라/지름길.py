'''
백준 1446

1. 세준이는 0에서 시작, d킬로미터까지 가야한다.
2. d가 10000보다 작거나 같기 때문에 d까지의 거리 하나하나를 노드로 본다.
3. 노드로 보았을때 일단 최소 거리는 for문을 통해 1로 초기화해준다. (노드 i에서 다음 노드 i+1까지의 거리는 1)
4. 이후 지름길의 정보가 들어오면 graph에 정보를 추가한다.

만약 지름길의 정보에서 지름길이 끝나는 지점이 목표지점 d보다 크면 (뒤로 돌아갈 수 없는 고속도로이므로) 정보를 추가하지 않는다
'''

from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heappop(q)
        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    

n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [INF] * (d + 1)

# 일단 거리 1로 초기화
for i in range(d):
    graph[i].append((i + 1, 1))

for i in range(n):
    a, b, c = map(int, input().split())
    if b > d: continue
    graph[a].append((b, c))

dijkstra(0)
print(distance[d])


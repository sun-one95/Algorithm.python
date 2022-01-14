import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

# 노드와 간선 개수 입력 받기
n, m = map(int, input().split())
# 노드들의 연결 관계를 가진 리스트 생성
graph = [[] for _ in range(n + 1)]
# 노드들의 최단거리 정보를 담을 리스트
distance = [inf] * (n + 1)
# 출발노드는 1번이라고 지정하였으므로
start = 1

# 간선 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    # 양방향이므로 각각 요소에 a 에서 b 까지의 거리를 1이라고 설정
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    distance[start] = 0 # 출발 노드로 부터의 거리는 0
    heapq.heappush(q, (0, start)) # q에다가 (거리, 노드) 삽입
    while q:
        dist, now = heapq.heappop(q)
        # 만약 방문한 노드라면, 패스
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))


dijkstra(start)
max_node = 0
max_distance = 0
result = []
for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)


print(max_node, max_distance, len(result))


from collections import deque

# 도시의 개수, 도로의 개수, 거리정보, 출발 도시번호
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]

# 도로 정보 받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1) # 모든 거리에 대한 리스트 -1로 초기화 설정
distance[x] = 0 # 출발점으로 부터의 거리를 0으로 재할당

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1: # 아직 방문하지 않았다면
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


# import sys
# from collections import deque

# n, m, k, x = list(map(int, sys.stdin.readline().split())) # n = 도시의 개수, m = 도로의 개수, k = 거리정보, x = 출발 도시의 번호
# graph = [[0] * (n + 1) for i in range(n + 1)] # [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

# for i in range(m):
#     start, end = map(int, sys.stdin.readline().split())
#     graph[start][end] = 1


# q = deque()
# for i in range(len(graph[x])):
#     if graph[x][i] == 1:
#         q.append()

# 너무 오랜만에 풀어서 그런지 버벅대고, 진행이 잘 안된다.

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

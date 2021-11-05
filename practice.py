from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]

# 도로 정보 입력하기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리 정보를 담은 리스트 선언, 기본값 -1로 설정
distance = [-1] * (n + 1) 
distance[x] = 0 # 출발점으로 부터의 거리를 0이라고 설정

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1: # 아직 방문하지 않았다면
            distance[next_node] = distance[now] + 1
            q.append(next_node)


check = False
for i in range(n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
    
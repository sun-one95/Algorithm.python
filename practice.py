from collections import deque

n, k = map(int, input().split())
graph = [] # 전체적인 맵의 정보를 담은 리스트
data = [] # 바이러스 정보를 담은 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0: # 바이러스일 경우
            # 바이러스 종류, 시간, x, y 위치를 삽입
            data.append((graph[i][j], 0, i, j))

data.sort() # 낮은 순서대로 바이러스 전염을 해야 하므로
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s: # 정해진 시간과 같으면 종료
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0: # 아직 방문하지 않았다면
                graph[nx][ny] = virus # 전염시작
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

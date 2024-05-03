# 백준 2206
from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능, [x][y][1]은 불가능
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

# 위, 우, 아래, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, z):    
    q = deque()
    q.append((x, y, z))
    # 큐가 진행되는 동안
    while q:
        a, b, c = q.popleft()
        # 끝점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    q.append((nx, ny, 1))
                # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    q.append((nx, ny, c))

    return -1

print(bfs(0, 0, 0))



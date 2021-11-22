n, m = int(input().split())
arr = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트
for i in range(n):
    arr.append(list(map(int, input().split())))

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 깊이 우선 탐색(DFS)를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에서 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 웊타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                count += 1
                dfs(count)
                arr[i][j] = 0
                count -= 1

dfs(0)
print(result)




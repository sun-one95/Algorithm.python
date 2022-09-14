# 이 문제는 일단 완전탐색으로 푼다.
# 초기 입력 받을 정보를 담을 리스트를 선언하고 그 안에 추가한다.
# 그리고 울타리를 설치할 때마다 그 안전영역의 개수를 세어야 하기 때문에 리스트를 하나 더 선언해준다.
# 무작위로 울타리를 세개 설치하고 나서 이제 바이러스가 전파 되고 난 후, 안전영역개수를 세어야 하므로
# 바이러스 전파되는 메서드를 따로 만들어주고, 안전영역개수를 세는 메서드도 만들어준다.


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




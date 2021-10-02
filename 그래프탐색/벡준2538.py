import sys
from collections import deque
# 리스트를 만들어서 기본값은 0이라고 세팅한후 직사각형이 있는 구역을 입력받으니까 그 구역을 1이라고 지정한다.
# 반복문을 통해 0인 구역을 함수로 보내서 1로 갱신하고 인접한 사각형을 세서 넓이를 만든다음 정답으로 쓸 리스트에다가
# 넣이를 넣어준다. 그 리스트의 길이가 영역의 개수가 되겠고, 요소각각이 넓이가 된다.


m, n, k = map(int, sys.stdin.readline().split())
l = [[0] * n for i in range(m)] # 모든 직사각형의 정보르 담은 리스트 선언

dy = [-1, 0, 1, 0]
dx = [0 , 1, 0, -1]

result = []


for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            l[j][k] = 1 # 직사각형이 있는 구역을 1로 할당


def bfs(s1, s2):
    q = deque()
    q.append([s1, s2])
    cnt = 1
    l[s1][s2] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n:
                if l[ny][nx] == 0:
                    l[ny][nx] = 1
                    cnt +=1 
                    q.append([ny, nx])
    
    result.append(cnt)
    

for i in range(m):
    for j in range(n):
        if l[i][j] == 0:
            bfs(i, j)

 
print(len(result))
result.sort()
for i in result:
    print(i, end=' ')

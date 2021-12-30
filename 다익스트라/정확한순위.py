inf = int(1e9)

# 노드와 간선 정보 받기
n, m = map(int, input().split())
# inf를 초기값으로 한 2차원 배열 선언
graph = [[inf] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 건 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력 받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for a in range(1, n + 1):
    cnt = 0
    for b in range(1, n + 1):
       if graph[a][b] != inf or graph[b][a] != inf:
           cnt +=1
    if cnt == n:
        result += 1
        
print(result) 

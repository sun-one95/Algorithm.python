import sys

inf = int(1e9)

# 노드의 개수 및 간선의 개수를 입력 받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[inf] * (n + 1) for i in range(n + 1)]

# 자기 자신에게 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for i in range(m):
    # A에서 B로 가는  비용은 C라고 실행
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == inf:
            print("infinite")
        else:
            print(graph[a][b], end=' ')

    print()
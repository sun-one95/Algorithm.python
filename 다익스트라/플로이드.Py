'''
우선 리스트를 만들어서 a에서 b로 가는 비용을 담을 리스트로 만든다.
그리고, 자기자신으로 가는 비용은 0으로 초기화 한다.
그리고 각 간선에 대한 비용 정보를 입력받아서 작은 값들로 초기화 시켜준다.
이제 다음 쉽게 말해 바로 가는 비용은 이제 최솟값들로 초기화 시켰으니
다음은, 경유해서 갈 때 가는 비용 중에 최솟값들로 저장해야 한다.
'''

inf = int(1e9)

n = int(input())
m = int(input())
graph = [[inf] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for k in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == inf:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
    
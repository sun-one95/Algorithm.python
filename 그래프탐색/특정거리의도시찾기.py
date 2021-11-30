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


"""
처음에는 인접행렬을 이용해서 일단 거리 정보들을 담은 다음에 거리리스트를 만들어서 1씩 증가시켜야 겠다고
생각 했다. 하지만, 코드 작성이 어려웠고, 추가 로직들이 생각이 나지 않았다.
이 문제는 인접리스트를 이용해 각 노드에 대한 연결되어있는 노드들을 담는다.
그리고 노드의 각 최단거리를 담은 리스트를 만들어서 초기값을 -1로 설정하고, 출발점에 대한 값을 0으로 설정한다.
왜냐면 이 말은 자기 자신으로 부터의 거리는 0이라는 뜻이다. 그 다음 큐를 만들어서 큐에 시작점을 추가한다.
그리고 반복문을 통해 맨 첫번째 원소를 추출하여, 추출한 노드의 인접 리스트 원소들을 반복문으로 뽑아낸다.
만약 방문하지 않았다면, 최단거리값은 현재 -1일 것이다. 그러면 걔내들의 값을 추출한 노드의 거리 값에서 1씩 더한다.
그 다음 다시 인접리스트에서 뽑은 노드를 큐에 삽입하여 반복문을 계속해서 돌린다.
반복문이 졸료되면 최단 거리 리스트가 완성이 되어있기 때문에 그 중 x와 같은 노드를 출력한다.
""" 
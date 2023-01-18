'''
백준 1766

위상정렬 알고리즘으로 문제를 푸는데, 여기서 추가로 원하는 점은
먼저 푸는 것이 좋은 문제가 있으면 그 문제를 풀고
다음 조건으로는 가능하면 쉬운 문제를 풀어야 한다.
그렇기 때문에 마지막 조건을 이행하려면 우선순위 큐를 사용하면 쉽게 풀 수 있다.
'''
import heapq

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동가능
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = [] # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    # 큐가 빌 때까지 반복
    while q:
        now = heapq.heappop(q)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                heapq.heappush(q, i)


    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

'''
n, m = 4, 2
indegree = [
    0
    1 - 1
    2 - 1
    3 - 0
    4 - 0
]
graph = [
    [],
    1 - [],
    2 - [],
    3 - [1],
    4 - [2],
]

result = []
q = [3, 4]
now = 3
result.append(3) = [3]
for i in graph[3]:
    i = (1)
    indegree[1] -= 1
    if indegree[1] = 0
'''
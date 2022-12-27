'''
백준 11403문제
플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해햐 하는 경우에 사용할 수 있는 알고리즘이다.

일단 입력값들을 다 입력받는다. 정점의 개수(노드개수) n 과 n개의 인접행렬을 입력받는다.
i번째 줄의 j번째 숫자가 1인 경우는 i에서 j로 가는 간선, 즉 길이 있다는 뜻이고, 0인 경우는 없다는 뜻이다.
자기 자신으로 가는 간선은 항상 0이다.

이제 입력받은 인접행렬의 배열을 삼중 반복문읉 통해 돌린다.
돌려서 i번째에서 j번째로 가는 길이 바로 있거나 (graph[i][j] = 1) 우회하여 i번째에서 k번째로 가는 길이 있고, k번째에서 j번째로 가는 길이 있다면,
둘 중 하나만 만족해도 1이라는 값을 할당한다.

그렇게 재할당한 graph배열을 다시 입력값 모양 처럼 리턴한다.
'''

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜 알고리즘
for k in range(n): # 경로 for 문이 가장 상위 단계여야 누락되지 않는다.
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


for row in graph:
    for col in row:
        print(col, end=" ")
    print()


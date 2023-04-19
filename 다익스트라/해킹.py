'''
백준 10282

문제가 약간 꼬아서 그렇지 핵심은 컴퓨터가 전염되는 과정이 마치 다익스트라 알고리즘의 개념인 간선 정보처럼 되어있다.
그러므로 다익스트라 알고리즘을 통해서 이 문제를 해결할 수 있다.

1. 다익스트라 알고리즘을 통햇 오염정보 리스트를 만든다.
2. distance 를 for 문을 돌려서 요소가 INF 가 아니라면 오염됐다는 의미이므로 카운트하고, 그 값이 현재 답으로 설정한 변수(time) 보다 큰지 비교한다.
3. 이 과정을 거치면 답을 도출할 수 있다.
'''
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        w, n = heappop(q)
        for n_n, wei in graph[n]:
            n_w = w + wei
            if n_w < distance[n_n]:
                distance[n_n] = n_w
                heappush(q, (n_w, n_n))

for tc in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in range(d):
        a, b, s = map(int ,input().split())
        graph[b].append((a, s))


    dijkstra(c)

    cnt = 0
    time = 0
    for i in distance:
        if i != INF:
            cnt += 1
            time = max(time, i)

    print(f'{cnt} {time}')






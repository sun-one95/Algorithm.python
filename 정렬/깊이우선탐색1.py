# 백준 24479

"""
파이썬으로 재귀를 사용해 문제를 풀 경우 특히, DFS, BFS 문제를 풀때 예시에서 답은 잘 나오는데, 정답 제출을 하면 런타임 에러를 접한다.

대부분이 파이썬의 재귀 최대 깊이의 기본 설정이 1,000회 이기 때문에 런타임 에러가 발생하는 경우이다..

이를 해결하기 위해서는 아래와 같이 코드를 작성해주면 된다.

import sys
sys.setrecursionlimit(10 ** 6)
"""

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

n, m, r = map(int, input().split())
line = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1
for i in range(m):
    u, v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)

dfs(r)
for i in range(1, n + 1):
    print(visited[i])


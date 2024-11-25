"""
백준 2644
"""

from collections import deque

def bfs(s):
    q = deque([s])
    visited[s] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                res[i] = res[v] + 1
                visited[i] = True

n = int(input())
s, d = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(s)
if res[d] > 0:
    print(res[d])
else:
    print(-1)
'''
백준 11725        
'''

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
# print(ans)
res = ans[2:]
for x in res:
    print(x)

'''
q = [1]

now = 1
graph[1] = [6, 4]
ans[6] == 0:
ans[6] = 1

q = [6]

ans[4] == 0:
ans[4] = 1

q = [6, 4]

now = 6
graph[6] = [1, 3]
ans[1] == 0:
ans[1] = 6

q = [4, 1]

ans[3] == 0:
ans[3] = 6

q = [4, 1, 3]

now = 4
graph[4] = [1, 2, 7]
ans[1] != 0

ans[2] == 0:
ans[2] = 4

ans[7] == 0:
ans[7] = 4

q = [1, 3, 2, 7]

now = 1
graph[1] = 6, 4
ans[6] != 0
ans[4] != 0

now = 3
graph[3] = 6, 5
ans[5] == 0:
ans[5] = 3

q = [2, 7, 5]




graph = [
    [],
    1 - [6, 4],
    2 - [4],
    3 - [6, 5],
    4 - [1, 2, 7],
    5 - [3],
    6 - [1, 3],
    7 - [4],
    []
]

ans = [
    0,
    1 - 6,
    2 - 4,
    3 - 6,
    4 - 1,
    5 - 3,
    6 - 1,
    7 - 4,
    8
]
'''
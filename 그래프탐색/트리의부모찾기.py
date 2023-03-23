'''
백준 11725

각 노드의 부모 노드 번호를 출력하는 문제이다.
처음에 너무 트리, 노드에 대한 개념이 없어서
이해하는데 어려웠다.

하지만, 단지 그 노드의 부모노드를 찾으면 되는것이었다. 노드의 개수는 n
입력값으로 연결된 두 정점이 n - 1개 주어진다.
이 정보를 인접리스트를 만들어서 거기에다가 저장을 해준다.

그다음 너비탐색을 통해서 1부터 먼저 시작해서 1과 연결된 노드들을 하나씩 확인하여
그 노드의 부모를 1로 지정한다.
위와 같은 방식으로 다른 노드들도 이렇게 진행한다.

내가 궁금했던 점은 큐를 쓰면 제일 작은 넘버인 노드를 뽑아내지 않아서 이게 답이 맞을 까 하는 생각을 했다.
하지만 부모노드로 나올 수 있는 값이 내가 봤을 때는 여러가지인데, 입력값 순서대로 진행을 했을 때, 나온 값이다.
만약 작은 넘버로 출력하라고 했으면 문제에서 명시되거나 그랬을 것이다. 
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
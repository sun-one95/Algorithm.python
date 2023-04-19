'''
백준 1939

두 개의 섬사이에 다리가 있는데, 그 다리에 운송할 있는 최대 무게 중량이 주어진다.
그래서 이 무게들 중에서 가장 최댓값을 리턴해야한다.

이 문제를 일단 이진탐색으로 어떻게 풀어야 했는지 어려웠다.
다익스트라 문제인가? 하고 생각도 했었다.

구하려는 최대 무게 값을 mid로 잛고 시작점과 끝점은 문제에서 주어진 범위를 보고 초기화했다.

이진탐색과 더불어 이 문제는 완전 탐색을 통해서 먼저 다 조회한 후 다음 이진탐색으로 넘어가야 한다.

1. 입력값들을 받아서 정리하는데, 다리가 연결된 섬과 섬 그리고 무게를 저장할 이차 배열 리스트를 만들어서 다익스트라 알고리즘 중에 이런 리스트가 있다. 양방향으로 넣어준다.
(bridges = [[] for _ in range(n + 1)])

2. 완전탐색 알고리즘을 짜는데, 조건을 큐에서 추출한 값(now)이 아까 만든 리스트 bridges를 이용하는데, bridges[now]를 반복문 돌리면 now와 연결된 섬의번호, 무게가 나온다. 
이러한 값들을 조건문을 통해 걸러준다.

3. 조건은 일단 방문리스트를 만들어줘서 한번 방문한 값은 True값으로 설정해준다. 기본값은 False이다. 만약 for문을 통해 나온 섬의 번호가 한번 방문한건지 아닌지 판별하고 아니라면,
그 무게가 현재 최댓값으로 잡은 무게보다 크거나 같은지 확인한다.

4. 조건에 부합하다면 큐에 그 섬번호를 삽입하고, 방문리스트를 True로 설정한다.

5. 다음은 이제 이진법 로직이다. mid값을 bfs(mid)로 돌려서 만약 그 값이 True이면 결과로 제출할 변수(result)에 mid값을 할당하고, start = mid + 1 해주고, 아니라면 
end = mid - 1로 해준다.

'''

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
bridges = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    bridges[a].append((b, c))
    bridges[b].append((a, c))

one, two = map(int, input().split())

def bfs(weight):
    q = deque()
    q.append((one))
    visited = [False] * (n + 1)
    visited[one] = True

    while q:
        now = q.popleft()

        for i, w in bridges[now]:
            if not visited[i] and w >= weight:
                visited[i] = True
                q.append(i)

    if visited[two]: return True
    else: return False

start = 1
end = 1000000000

result = 0
while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
    
    

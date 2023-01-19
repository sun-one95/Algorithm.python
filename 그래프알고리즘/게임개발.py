from collections import deque   

n = int(input())
time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)] # 건물들의 건설시간
indegree = [0] * (n + 1)
dp = [0] * (n + 1) # 해당 건물까지 걸린 시간

arr = []
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in range(1, len(data) - 1):
        indegree[i] += 1
        graph[data[j]].append(i)

# print(time)
# print(graph)
# print(indegree)


q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[now] + time[i], dp[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, len(dp)):
    print(dp[i])

'''
time = 
[
    1번 - 10
    2번 - 10
    3번 - 4
    4번 - 4
    5번 - 3
]

graph = [
    1번 - []
    2번 - [1]
    3번 - [1]
    4번 - [3, 1]
    5번 - [3]
]

indegree = [
    1번 - 0
    2번 - 1
    3번 - 1
    4번 - 2
    5번 - 1
]

dp = [
    1번 - 10,
    2번 - 0,
    3번 - 0,
    4번 - 0,
    5번 - 0
]

q = [1]
dp[1] = time[1] = 10

while q:
    now = q.popleft() = 1, q = []
    for i in graph[now]:


'''
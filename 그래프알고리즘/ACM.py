from collections import deque
 
 
for tc in range(int(input())):
    n, k = map(int, input().split()) 
    time = [0] + list(map(int, input().split()))#건물들의 건설시간
    graph = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)
    DP = [0] * (n + 1) #해당 건물까지 걸리는 시간
 
    for _ in range(k):#건설순서규칙 저장
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b]+=1
 
    q = deque()
    for i in range(1, n+1): #진입차수 0인거 찾아서 큐에 넣기
        if indegree[i] == 0:
            q.append(i)
            DP[i]=time[i]
 
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i]-=1#진입차수 줄이고
            DP[i]=max(DP[now]+time[i],DP[i])#DP를 이용해 건설비용 갱신
            if indegree[i]==0:
                q.append(i)

    w = int(input())
    print(DP[w])


'''
백준 1005번
time = 
[
    1번-10,
    2번-1,
    3번-100,
    4번-10
]
indegree = 
[
    0번-0, 
    1번-0, 
    2번-1, 
    3번-1, 
    4번-2
] 
graph = 
[
    [], 
    1번-[2, 3], 
    2번-[4], 
    3번-[4], 
    4번-[]
]
dp =
[
    0,
    1번 - 10,
    2번 - 11,
    3번 - 110,
    4번 - 21
]
w = 4

now = 1
graph[1] = [2, 3]
indegree[2] -= 1
dp[2] = max(dp[1] + time[2], dp[2]) = 11
indegree[3] -= 1
dp[3] = max(dp[1] + time[3], dp[3]) = 110
indegree = 
[
    0번-0, 
    1번-0, 
    2번-0, 
    3번-0, 
    4번-2
]
q = [2, 3]

now = 2
graph[2] = [4]
indegree[4] -= 1
dp[4] = max(dp[2] + time[4], dp[4]) = 21

now = 3
graph[3] = 4
indegree[4] -= 1
dp[4] = max(dp[3] + time[4], dp[4]) = 120

print(dp[4]) = 120

n, k = 8, 8
build_time = 
[
    1번-10, 
    2번-20, 
    3번-1, 
    4번-5,
    5번-8,
    6번-7, 
    7번-1,
    8번-43
]
indegree = [0, 1번-0, 2번-1, 3번-1, 4번-1, 5번-1, 6번-1, 7번-2, 8번-1]
graph =[
    [], 
    1번-[2, 3], 
    2번-[4, 5], 
    3번-[6], 
    4번-[], 
    5번-[7], 
    6번-[7], 
    7번-[8], 
    8번-[]
]
7 6 3 1 = 1 + 7 + 1 + 1 = 39
7 5 2 1 = 1 + 8 + 20 + 10 = 39
7번까지 가려면 7번 진입차수가 0이 되어야한다. 7번 = 1
-> 5번 6번 처리(8, 7) = 8
-> 5번 6번 까지 가려면 마찬가지로 이들의 진입차수가 0이 되어야 한다.
-> 2번 3번 처리(20, 1) = 20
-> 2번 3번 까지 가려면 마찬가지로 이들의 진입차수가 0이 되어야 한다.
-> 1번 처리 = 10
-> 39
w = 7
time = 0

indegree[1] = 0
q.append(1)
time += build_time[1 - 1] = 10

now = 1
graph[1] = [2, 3]
indegree[2] -= 1
indegree[3] -= 1
indegree = [0, 0, 0, 0, 1, 1, 1, 2, 1]
time_arr.append(build_time[1])
time_arr.append(build_time[2])
time_arr = [0, 20, 1]
time += max(time_arr) = 30


'''
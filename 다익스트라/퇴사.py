'''
백준 14501


45만원 겟

상담을 시작하는 날짜를 하나하나씩 대보면서 일일히 상담을 했을 때, 발생하는 총 비용들을 따로 리스트를 만들어줘서 거기안에다가 넣어주고
마지막에 최댓값을 추출하면 될듯하다.

상담을 시작하는 날짜 변수 date 변수 설정

'''

# n = int(input())
# schedule = []
# for i in range(n):
#     t, p = map(int, input().split())
#     schedule.append((t, p))

# dp = [0 for i in range(n + 1)]

# for i in range(n):
#     for j in range(i + schedule[i][0], n + 1):
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]

# print(dp[-1])


n = int(input())
arr = []
for i in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if i + arr[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])

print(dp[0])



    


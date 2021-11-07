# n x m 크기의 금광에서 첫 출발은 첫 번째 열의 어느 행이든 출발하여 m번에 걸쳐 이동을 하는데, 그 이동도 오른쪽, 오른쪽 위, 오른쪽 아래 셋 중 하나를 택하여 이동해야한다.
# 최대로 금광을 가질 수 있도록 이동을 해야 하므로, 출발을 할 때도 각 열의 최대를 가지는 행을 택하여 이동하고, 다음도 최댓값을 가지는 행으로 이동을 해야한다.
# [[0, 0, 0, 0, 0], [0, 1, 3, 3, 2], [0, 2, 1, 4, 1], [0, 0, 6, 4 7]]
# tc = int(input())
# for i in range(tc):
#     n, m = map(int, input().split())
#     gold_road = [[0 for i in range(m + 1)] for j in range(n + 1)]

#     gold_information = list(map(int, input().split()))
#     cnt = 0
#     for j in range(1, n + 1):
#         for k in range(1, m + 1):
#             gold_road[j][k] = gold_information[cnt]
#             cnt += 1

#     ans = 0
#     for b in range(1, m + 1):
#         ans = max(ans, gold_road[b])

tc = int(input())
for i in range(tc):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)


# j = 1, i = 0 일 때,
# left_up = 0, left_down = dp[1][0], left = dp[0][0]
# dp[0][1] = dp[0][1] +  2 = 5
#  
'''
백준 14003

기존에 풀었던 가장 긴 증가하는 부분 수열보다 범위가 늘어났다.
수열 중에 음수가 추가되어서 조금 추가 장치를 더해 문제를 풀어야 한다.

1. 입력값으로 n개의 수열을 입력받는데, 거기서 [0]을 추가해준다.
2. 리스트(dp)를 만들어줘서 각 요소의 현재 연속적으로 증가하는 수열의 개수로 채울 것이다.
3. 증가하는 수열을 담을 리스트(result)를 만들어준다. 초기값으로 범위의 음수보다 적은 값으로 채워준다.
4. 1부터 n까지 for문을 돌려서 result[-1]에 위치한 요소값보다 큰지 작은지 확인하낟.
크다면 result에 그 값을 추가해주고 아니라면, 현재 result 마지막 요소 값보다 작거나 같다는 뜻이다.
그러므로 그 값이 현재 result 에 있는지 확인하여 그 위치에 넣어준다. 없다면 어차피 0이라고 뜰것이므로 그 자리에 이 값을 갱신한다.
5. 여기까지 과정을 거치면 연속하는 증가하는 수열의 개수를 구할 수 있다.
6. 하지만 이제 연속으로 증가하는 수열을 이제 나열해야 하는데, 예제를 보니까 지금 풀이대로 하면 원하는 값을 구하기 어렵다.
7. 그러므로 로직을 추가해준다. 아래에
8. 하나는 dp의 최고값을 담을 변수(max_idx, 이 변수가 의미하는 바는 연속으로 증가하는 수열의 최고 길이)와 증가하는 수열을 담을 리스트(ans)를 만들어 준다.
9. 반복문을 내림차순으로 돌려서(n부터 1까지) dp[i] 가 max_idx - 1와 같은지 확인하고 같다면 ans에 추가해주고
max_idx를 dp[i]값으로 갱신해준다.
10. 위와 같은 과정을 하면 원하는 결과값을 도출할 수 있다.
'''

from bisect import bisect_left

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
result = [-float('inf')]

for i in range(1, n + 1):
    if result[-1] < arr[i]:
        result.append(arr[i])
        dp[i] = len(result) - 1
    else:
        dp[i] = bisect_left(result, arr[i])
        result[dp[i]] = arr[i]

print(len(result) - 1)

max_idx, ans = max(dp) + 1, []
for i in range(n, 0, -1):
    if dp[i] == max_idx - 1:
        ans.append(arr[i])
        max_idx = dp[i]

print(*ans[::-1])

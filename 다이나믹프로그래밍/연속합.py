'''
백준 1912

n개로 이루어진 임의의 수열 중에서 연속된 몇개의 수를 선택해서 나올 수 있는 합 중에서 가장 큰 값을 찾아야햔다.

다이나믹 프로그래밍으로 풀려면
선언해주는 dp 리스트에 값들은 아마도 인덱싱 넘버의 의미를 예를 들면 1이면 1개만으로 뽑았을 때 나올 수 있는 최댓값 이런 의미로 생각해볼 까?

내가 푼 풀이
- 이중 반복문을 돌려서 첫 반복문의 의미는 i개를 더할 때 나올 수 있는 최댓값을 의미한다.
- 두번째 반복문은 이제 그 연속하는 i번째 까지 요소들을 합한 경우이며 arr[j: j + i] 이렇게 해서 나온 값들을 대소 비교하여 구했다.
- 마자막에 max(dp)를 출력하여 최댓값을 리턴하게 하였다.
- 하지만, 아무래도 정수의 범윅가 10의 5까지 여서 이중 반복문을 돌리면 10의 10까지 늘어나서 시간초과에 걸렸다.

새로운 풀이
- 처음에 sum이라는 리스트를 만들어줘서 그 안에 첫번째 인덱스 값에 주어진 입력 리스트인 arr[0]을 넣어준다.
- sum의 i 번째 인덱스와 arr의 i + 1번째 인덱스의 숫자를 합한 값과 arr의 i + 1번째 숫자를 비교하여 더 큰 숫자를 sum리스트에 넣어준다.
- 이렇게 하면 효율적으로 연속하는 최댓값을 구할 수 있다는 사실을 알았다.

'''

import sys

input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [-1000] * (n + 1)

# for i in range(1, n + 1):
#     for j in range(n + 1):
#         sum_value = sum(arr[j:j+i])
#         if sum_value > dp[i]:
#             dp[i] = sum_value

# print(max(dp))

n = int(input())
arr = list(map(int, input().split()))
sum = [arr[0]]
for i in range(n - 1):
    sum.append(max(sum[i] + arr[i + 1], arr[i + 1]))
print(max(sum))

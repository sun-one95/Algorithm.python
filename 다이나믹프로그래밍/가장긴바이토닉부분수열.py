"백준 11054"
"""
각 인덱스별로 증가하는 수열길이 + 감소하는 수열 길이의 합이 가장 큰 지점이 바이토닉 수열의 sk원소가 된다.
즉, 주어진 수열에서의 바이토닉 수열은 1, 2, 3, 4, 5, 2, 1가 되며, sk는 5가 된다.
증가하는 수열: 1,2,3,4,5
감소하는 수열: 5,2,1
합을 구하면서 주어진 수열의 8번째 원소인 5를 두 번 계산하였으므로 1을 빼주면 정답을 구할 수 있다.
"""

import sys
input = sys.stdin.readline

x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(x)] # 가장 긴 증가하는 부분수열
decrease = [1 for i in range(x)] # 가장 긴 감소하는 부분수열(reversed)

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] - 1

print(max(result))


"""
위의 코드는 가장 긴 증가하는 부분 수열을 계산하면서, 가장 긴 감소하는 부분 수열도 같이 알아내기 위해서 주어진 수열을 reverse 시켰다. 대신,
dec에는 인덱스가 반대로 들어가있으므로, 다시 한 번 바꿔서 생각해줘야 한다.

이 방법이 헷갈린다면 for문을 역방향으로 돌려 가장 긴 감소하는 부분 수열을 구하는 방법도 있다.

import sys
input = sys.stdin.readline

x = int(input())
case = list(map(int, input().split()))

inc = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            inc[i] = max(inc[i], inc[j] + 1)

dec = [1 for i in range(x)]
for i in range(x-1, -1, -1):
    for j in range(x-1, i, -1):
        if case[i] > case[j]:
            dec[i] = max(dec[i], dec[j] + 1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = inc[i] + dec[i] - 1

print(max(result))
"""
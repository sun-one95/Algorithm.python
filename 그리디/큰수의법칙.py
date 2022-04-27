# 내림차순 정렬 시켜서 큰 수 더하고 그 다음에 작은 수  큰 수 이런 식으로 더하자

import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr, reverse = True)
first = arr[0]
second = arr[1]


result = 0
cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)

result += cnt * first
result += (m - cnt) * second
   
print(result)
import sys

n, m = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))

# 이분탐색 전 초기값 설정
start = 0
end = max(l)

# 이분탐색 시작
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in range(len(l)):
        if l[i] > mid:
            total += l[i] - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

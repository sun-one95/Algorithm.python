import sys

k, n = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(k):
    l.append(int(sys.stdin.readline()))


start = 1
end = max(l)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in range(k):
        total += l[i] // mid

    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1


print(result)


import sys

n = int(sys.stdin.readline())
array_A  = list(map(int, sys.stdin.readline().split()))
array_B  = list(map(int, sys.stdin.readline().split()))

array_A.sort()
array_B.sort(reverse=True)

cnt = 0
for i in range(n):
    cnt += array_A[i] * array_B[i]

print(cnt)
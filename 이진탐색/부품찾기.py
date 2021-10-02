import sys

n = int(sys.stdin.readline())
array_N = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
array_M = list(map(int, sys.stdin.readline().split()))

def bs(l, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return bs(l, target, start, mid - 1)
    else:
        return bs(l, target, mid + 1, end)

for i in range(m):
    result = bs(array_N, array_M[i], 0, n - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
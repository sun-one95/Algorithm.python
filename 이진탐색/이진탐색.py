import sys

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
    
n, target = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))

result = bs(l, target, 0, n - 1)
if result == None:
    print('찾는 원소가 없습니다.')
else:
    print(result + 1)
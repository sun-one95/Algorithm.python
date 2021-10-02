import sys

def bs(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bs(array, target, start, mid - 1)
    else:
        return bs(array, target, mid + 1, end)

n = int(sys.stdin.readline())
array_n = list(map(int, sys.stdin.readline().split()))
array_n.sort()
m = int(sys.stdin.readline())
array_m = list(map(int, sys.stdin.readline().split()))

# m의 정수 들 중에 하나씩 따와서 그게 n의 정수와 같은지 확인하는 여부
# 이분탑색을 이용해서 풀어야 할듯
# 반복문을 통해 array_n에 타켓인 array_m[i]가 있는 지 확인
for i in range(m):
    result = bs(array_n, array_m[i], 0, n - 1)
    if result == None:
        print(0, end=" ")
    else:
        print(1, end=" ")
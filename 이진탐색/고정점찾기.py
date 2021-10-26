import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))



def bs(arr, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        # arr[mid] 값이 mid보다 클 경우
        elif arr[mid] > mid:
            end = mid - 1
        # arr[mid] 값이 mid보다 작을 경우
        else:
            start = mid + 1
    return None

index = bs(arr, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)
'''
백준 1920 - 수찾기
전형적인 이진법 탐색 문제
이진법 알고리즘을 사용해서 타겟숫자가 있는지 없는지 확인한다.
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
targets = list(map(int, input().split()))


def bs(arr, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None



for target in targets:
    result = bs(data, target, 0, n - 1)
    if result == None:
        print(0)
    else:
        print(1)
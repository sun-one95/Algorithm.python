import sys

n, x = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

cnt = [0] * (max(arr) + 1) # arr 요소들의 중복 개수 세는 리스트 만들기
for i in range(len(arr)):
    cnt[arr[i]] += 1

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

result = bs(arr, x, 0, n - 1)
if result == None: # 없다면 -1 출력
    print(-1)
else: # 있다면 그 원소의 개수를 출력 해야 하므로 아래와 같이 표현
    print(cnt[arr[result]])

'''
# 참조 풀이
# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, k):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] > target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return last(array, target, mid + 1, end)

# 값이 x인 데이터의 개수 계산
count = count_by_value(arr, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
else:
    print(count)
'''
'''
# 참조 두번째 풀이
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_right(array, left_value)
    return right_index - left_index

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(arr, x, x)

# 값이 x인 원소가 존재하지 않는다면 
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
'''

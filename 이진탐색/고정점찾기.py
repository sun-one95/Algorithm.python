import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))



def bs(arr, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        # arr[mid] 값이 mid보다 클 경우 mid 이후 영역은 볼 필요가 없음
        elif arr[mid] > mid:
            end = mid - 1
        # arr[mid] 값이 mid보다 작을 경우 mid 이전 영역은 볼 필요가 없음
        else:
            start = mid + 1
    return None

index = bs(arr, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)

'''
여기서 고정점이란, 인덱스와 인덱스의 위치한 값이 같을 때를 고정점이라 한다.
이진탐색을 통해 고정점을 구한다. 타겟팅하는 값은 각각의 인덱스 넘버이다.
만약 중간점의 값과 중간점이 같다면 바로 그 값을 리턴하면 된다.
그런데, 중간점의 값이 중간점보다 크다면 왼쪽 영역을 탐색하면된다. 왜냐면, 그 이후는 어차피 이제 고정점이 나오지 않기때문이다.
반대로 중간점의 값이 중간점보다 작다면 오른쪽 영역을 탐색하면 되는것이다.
'''
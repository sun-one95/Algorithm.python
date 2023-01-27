'''
백준 2470

이 문제는 이진 탐색개념이 조금 들어가는 것 같다.
일단 입력받은 배열을 오름차순 정렬 시키고

start, end 를 지정하여 첫 인덱스와, 끝 인덱스로 값을 지정한다.
그런 다음 min_val = INF 로 지정하고 
무한 반복문을 돌려서 arr[start] + arr[end] 의 절댓값이(-는 무조건 작기때문에 절댓값 처리) min_val 값보다 작다면
min_val 값을 갱신한다.

그리고 만약 더한 값이 0보다 크다면 0에 근접한 값을 찾아야 하기 때문에
end = mid - 1 로 줄여주고
그 반대라면 start = mid + 1로 늘려준다.
'''

import sys

INF = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = n - 1

pair = []
min_val = INF
while start < end:
    total = arr[start] + arr[end]
    if abs(total) < min_val:
        min_val = abs(total)
        pair = (arr[start], arr[end])

    if total >= 0:
        end -= 1
    else:
        start += 1

print(*pair)



 
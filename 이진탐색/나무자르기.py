'''
이 문제는 절단기 높이 지정을 이진법을 통해서 찾아야 한다.
주어진 나무들의 높이를 오름차순 정렬하여 가장 낮은 높이와 높은 높이의 중간점을 시작으로
절단기 높이로 임시 지정한다. 그래서 그 높이에 맞게 나무를 절단하여 가져가는 높이의 합들이 M보다 크거나 같다면 리턴한다.
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if mid < i:
            total += (i - mid)
    
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
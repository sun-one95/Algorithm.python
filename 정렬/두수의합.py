'''
백준 3273

일반 정렬로 문제를 풀려고 했는데 시간 복잡도가 문제여서 더 효율적인 알고리즘으로 풀어야 했다.
그래서 이진탐색을 택했고 근데 내가 쓴 풀이로 진행을 하게 되면 같은 쌍이 두번 반복 더해지기 때문에
마지막에 2로 나눈 값을 출력 했다.
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

cnt = 0
arr.sort()
for i in range(len(arr)):
    a = arr[i]
    target = x - a
    if bs(arr, target, 0, n - 1) != None:
        cnt += 1

print(cnt // 2)
    

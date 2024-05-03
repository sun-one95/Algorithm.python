'''
백준 8979
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key= lambda x: (x[1], x[2], x[3]), reverse=True) # 금, 은, 동 순으로 정렬한 배열

idx = [arr[i][0] for i in range(n)].index(k) # k와 같은 번호를 가진 배열의 현재 등수

# 반복문을 돌려서 idx보다 높은 순위가 몇개인지 찾은 후 그 개수에 + 1을 하면 idx의 등수이다. (금은동 개수가 동률인 경우도 무조건 같은 등수로 리턴)
for i in range(n):
    if arr[idx][1:] == arr[i][1:]:
        print(i+1)
        break


'''
백준 2075

arr = [
    5 7 9 12 15
    6 8 11 13 19
    10 16 21 26 31
    14 25 28 35 48
    20 32 41 49 52
]

ans = [
                15
             13 19
          21 26 31
       25 28 35 48 
    20 32 41 49 52
]

'''
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    arr.append(data[:i + 1])


ans = []
for i in range(n):
    for j in range(len(arr[i])):
        ans.append(arr[i][j])

ans.sort(reverse=True)
print(ans[n - 1])

'''
백준 10867
'''

n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(n):
    if arr[i] not in result:
        result.append(arr[i])

result.sort()
for i in result:
    print(i, end=' ')
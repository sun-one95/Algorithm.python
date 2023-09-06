'''
백준 1940
'''

# n = int(input())
# m = int(input())
# arr = list(map(int, input().split()))

# arr.sort()
# cnt = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] + arr[j] == m:
#             cnt += 1

# print(cnt)

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()
left, right = 0, n-1
cnt = 0

while left < right:
    sum = arr[left] + arr[right]
    if sum > m:
        right -= 1
    elif sum < m:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)


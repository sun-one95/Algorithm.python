import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

# arr.sort()
# for i in range(len(arr)-1, -1, -1):
#     print(arr[i], end=' ')
result = sorted(arr, reverse=True)

for i in result:
    print(i, end=" ")
# 백준 25304

x = int(input())
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    c = a * b
    arr.append(c)

sum = 0
for i in range(n):
    sum += arr[i]

if  x == sum:
    print('Yes')
else:
    print('No')
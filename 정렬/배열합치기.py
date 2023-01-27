'''
백준 11728
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))    
for i in range(m):
    a.append(b[i])

a.sort()
for i in a:
    print(i, end=' ')
    
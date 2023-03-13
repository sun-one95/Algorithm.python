'''
백준 2869
'''

a, b, v = map(int, input().split())

cnt = 0
sum = 0
while True:
    cnt += 1
    sum += a
    if sum >= v:
        break
    sum -= b

print(cnt)
    

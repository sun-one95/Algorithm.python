'''
백준 10162

거스름돈 문제랑 비슷하게 풀면 될듯하다.
'''

n = int(input())

time_types = [300, 60, 10]
result = []

for time in time_types:
    result.append(n // time)
    n %= time

if n != 0:
    print(-1)
else:
    for i in result:
        print(i, end=' ')
# print(5 % 2) # 1
# print(5 / 2) # 2.5
# print(5 // 2) # 2

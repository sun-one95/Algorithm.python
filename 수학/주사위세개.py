'''
백준 2480

1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)x1,000원의 상금을 받게 된다. 
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)x100원의 상금을 받게 된다. 
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)x100원의 상금을 받게 된다.  
'''

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 1번째 규칙인 경우
if a == b and b == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (a * 100))
elif a == c:
    print(1000 + (a * 100))
else:
    print(max(a, b, c) * 100)




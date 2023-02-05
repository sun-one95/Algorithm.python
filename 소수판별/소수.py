'''
백준 2581

m이상 n이하의 자연수중 소수를 찾아서 그 들의 합과 그리고 가장 작은 최솟값을 리턴하는 문제다.
'''

import math

m = int(input())
n = int(input())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

result = []
isPrime = False
for i in range(m, n + 1):
    if i == 1:
        continue
    if is_prime_number(i):
        isPrime = True
        result.append(i)

if not isPrime:
    print(-1)
else:
    print(sum(result))
    print(result[0])

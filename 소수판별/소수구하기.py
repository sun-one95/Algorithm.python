'''
백준 1929

m이상 n이하의 수 중 소수인걸 찾아서 나열하면 된다.
'''
import math

m, n = map(int, input().split())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

for i in range(m, n + 1):
    if i == 1:
        continue
    elif is_prime_number(i):
        print(i)
'''
백준 1978
'''
import math

n = int(input())
arr = list(map(int, input().split()))

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

cnt = 0
for i in range(n):
    if arr[i] == 1:
        continue
    elif is_prime_number(arr[i]):
        cnt += 1

print(cnt)

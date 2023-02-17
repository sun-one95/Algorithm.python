'''
백준 4948

소수판별 알고리즘을 짜서
주어진 n에서 2n까지의 정수중에 소수가 몇개인지 구하면된다.
'''
import math

def is_prime_number(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False

        return True

while True:
    n = int(input())
    if n == 0:
        break
    
    if n == 1:
        print(1)
    else:
        cnt = 0
        for i in range(n+1, 2*n + 1):
            if is_prime_number(i):
                cnt += 1
        print(cnt)
                
   




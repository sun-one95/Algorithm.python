import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))

'''
a, b  = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

최소공배수는 두수를 곱한값을 두수의 최대공약수로 나눈 값이다.
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

'''

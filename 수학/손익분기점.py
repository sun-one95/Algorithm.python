'''
백준 1712

고정비용(A) = 1000만원
가변비용(B) = 1대당 70만원

ex)
노트북 가격(C) = 170만원
노느북 개수(n) = 미정

A + (B * n) < C * n 이 되는 시점을 구해야 한다.

1000 + 70n < 170n
1000 < 100n
10 < n 이므로 n = 11

3 + (2 * n) < 1 * n
3 < -n
'''
import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    n = a // (c - b)
    n += 1

    print(n)
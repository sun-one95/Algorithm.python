n, k = map(int, input().split())

result = 0
while n != 1:
    # n이 k로 나누어 떨어질때
    if n % k == 0:
        n = n // k
    else:
        n -= 1
    result += 1

print(result)
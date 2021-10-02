import sys

n = int(sys.stdin.readline())
change_money = 1000 - n

money_types = [500, 100, 50, 10, 5, 1]
cnt = 0
for money in money_types:
    cnt += change_money // money
    change_money %= money

print(cnt)
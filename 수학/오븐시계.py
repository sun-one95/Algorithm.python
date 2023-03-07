a, b = map(int, input().split())
c = int(input())

hour = a
min = b + c
if min >= 60:
    hour += (min // 60)
    min %= 60
    if hour >= 24:
        hour -= 24

print(hour, min)
    

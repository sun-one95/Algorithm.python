'''
지원 가능 총 예산: 485
[110, 120, 140, 150]
start = 110
end = 150
mid = 130
최대 130까지 지원
-> [110, 120, 130, 130] => 490 (예산 초과 부적합)

start = 110
end = mid - 1 = 129
mid = 229/2 = 114
최대 114까지 지원
-> [110, 114, 114, 114] => 452 (예산 적합, 하지만 여유있음)

start = mid + 1 = 115
end= 129
mid = (244) // 2 = 122
최대 122까지 지원
-> [110, 120, 122, 122] = 474 (아직 부족)

start = mid + 1 = 116
end = 129
mid = (116 + 129 = 245) // 2 = 122 (아까랑 mid값이 같기 때문에 부적합)

start = mid + 1 = 117
end = 129
mid = 246 // 2 = 123
최대 123까지 지원
-> [110, 120, 120, 120] = 470 (아직 부족)

start = mid + 1 = 118
end = 129
mid = 247 // 2 = 123 (값이 위와 동일)

start = mid + 1 = 119
end = 129
mid = 248 // 2 = 124
최대 124까지 지원
=> [110, 120, 124, 124] = 478(아직 부족)

start = mid + 1 = 120
end = 129
mid = 249//2 = 124 (위와 동일)

start = mid + 1 = 121
end = 129
mid = 250 = 125
최대 125까지 지원
-> [110, 120, 125, 125] = 480(부족)

start = mid + 1 = 122
end = 129
mid = 251 = 125 (위와 동일

start = mid + 1 = 123
end = 129
mid = 252 // 2 = 126
최대 126까지 지원
-> [110, 120, 126, 126] = 482(부족)

start = 125
end = 129
mid = 254 = 127
최대 127까지 지원
-> [110, 120, 127, 127] = 484

start = 127
end = 129
mid = 256 = 128
-> [110, 120, 128, 128] = 48


'''

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()
start = 0
end = arr[-1]
result = 0

while (start <= end):
    sum_value = 0
    mid = (start + end) // 2
    for i in range(n):
        if mid < arr[i]:
            sum_value += mid
        else:
            sum_value += arr[i]

    if sum_value <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
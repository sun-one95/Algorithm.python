n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0 # 그룹의 총수

count = 0 # 현재 그룹에 포함된 모험가의 수

for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
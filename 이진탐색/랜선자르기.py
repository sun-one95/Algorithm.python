'''
백준 1654 문제

0 ~ 802 => mid = 401

802 -> 2개
743 -> 1개
457 -> 1개
539 -> 1개

총 5개  -> 6개 부족

end = mid - 1 = 400
mid = 200

802 -> 4개
743 -> 3개
457 -> 2개
539 -> 2개

총 11개 -> 성립

위의 예시처럼 문제 풀면 될듯
'''

k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

arr.sort()

start = 0
end = arr[-1]
result = 0

while (start <= end):
    count = 0
    mid = (start + end) // 2
    for i in arr:
        if i >= mid:
            count += (i // mid)
    
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
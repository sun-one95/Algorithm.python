'''
백준 2292

1 (1)
6 (2 - 7)
12 (8 - 19)
18 (20 - 37)
24 (38 - 61)

1. 규칙이 맨처음을 제외하고는 6씩 증가한다.
2. 그러므로 시작점을 1로 잡고 만약 주어진 n이 이 시작점보다 작거나 같다면 그 범위안에 있는거다.
3. 아니라면 시작점을 (6 * 사이클 수) 갑에 더하여 계속해서 찾아나간다.
4. 사이클 수는 처음에는 1로 지정하고 1씩 더해줘서 넓혀준다.

'''

n = int(input())
num = 1
i = 1
cnt = 1
while True:
    if n <= num:
        break
    num += (6 * i)
    i += 1
    cnt += 1

print(cnt)



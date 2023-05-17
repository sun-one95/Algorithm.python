'''
백준 1072

게임횟수(x)와 이긴 게임(y), 승률(z)이 주어지는데,
여기서 승률을 높이려면 최소 몇번을 이겨야 하는지 구해야 한다.

그래서 이진탐새을 통해서 mid값을 최소승수라고 정하고
시작점은 0, 끝점은 x로 지정한다.

1. 만약 승률이 99이상이면 불가능하다. 왜냐면 100프로로 올려야 하기 때문에
그전에 다 이겼어야 하기때문에 패가 없어야 하기 때문에 이건 불가능(-1출력)

2. mid를 추가한 승률이 z보다 작거나 같다면 시작점을 mid + 1로 올린다.

3. 아니라면 답이다.
'''
import sys
input = sys.stdin.readline
 
 
X, Y = map(int, input().split())
Z = (Y * 100) // X
if Z >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = X
 
    while left <= right:
        mid = (left + right) // 2
        if (Y+mid)*100 // (X+mid) <= Z:
            left = mid+1
        else:
            answer = mid
            right = mid - 1
 
    print(answer)
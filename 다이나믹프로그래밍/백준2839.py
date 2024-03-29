'''
3과 5로 딱 떨어지는 설탕의 무게 봉투 그중 최솟값을 리턴해야한댜.
나누어 떨어지지 않는 경우는 -1로 정했다.
미리 기본값을 정해야 하는데 이 부분이 어려웠던게 나는 d[3]과 d[5]의 값을 정하고 그 사이값인 d[4]
까지 정했다. 하지만 내가 세운 식 d[i] = min(d[i - 3] + 1, d[i - 5] + 1) 이 6일 때 오류가 발생했다.
왜냐면 내가 1과 2일 때의 값은 아예 0으로 지정(왜냐면 3으로 나누어 떨어지지도 않고 작기 때문에) 지정해놔서
이들이 식에 값으로 나타나게 되면 최솟값이 이들이 될 것이기에 얘네들이 안나타게 미리 기본값을 더 설정해 줘야 했다.

'''

import sys

n = int(sys.stdin.readline())
d = [0 for i in range(5001)]
d[3] = 1
d[4] = -1
d[5] = 1
d[6] = 2
d[7] = -1
d[8] = 2
d[9] = 3
d[10] = 2
d[11] = 3
d[12] = 4
for i in range(13, 5001):
    d[i] = min(d[i-3] + 1, d[i-5] + 1)

print(d[n])


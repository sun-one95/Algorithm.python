"""
백준 9251

acaykp
capcak

s1  a
s2  c, ca, cap, capc, capca, capcak
=>  0, 1,  1,   1,    1,     1

s1 ac
s2 c, ca, cap, capc, capca, capcak
=> 1, 1,  1,   1,    1,     1

s1 aca
s2 c,  ca, cap, capc, capca, capcak
=> 1,  2,  2,   2,    2,     2

s1 acay
s2 c,  ca, cap, capc, capca, capcak
=> 1,  2,  2,   2,    2,     2

s1 acayk
s2 c,   ca, cap, capc, capca, capcak
=> 1,   2,  2,   2,    3,     4

s1 acaykp
s2 c,    ca, cap, capc, capca, capcak
=> 1,    2,  3,   3,    3      4

s1 ac
sc c

s1 ac
sc capc
두 상황에서 s1의 c와 s2의 c가 같다
=> 비교하는 글자가 있기 바로전까지의 lcs + (현재 문자를 비교한 결과가 같으면 1, 다르면 0)

s1: a c
s2: cap c
의 바로 이전까지의 lcs는 현재 비교하고 있는 c가 있기 전인

s1 a
s2 cap
까지의 lcs이다.

따라서, 현재 문자를 비교했을 때 같다면 바로 이전까지의 lcs에 +1을 해주고,
같지 않다면, 비교 이전까지의 lcs를 갖고 있으면 된다.

2차원 행렬을 만들어 표로 보는 것이 규칙을 찾고 점화식을 만들때 더욱 편하다.
    c   a   p   c   a   k
a
c
a
y
k
p

2차원 행렬로 lcs[i][j]라고 표현할 때, 바로 이전까지의 lcs는 lcs[i-1][j-1] 임을 알 수 있다.
따라서 비교한 문자가 같은 경우,
lcs[i][j] = lcs[i-1][j-1] + 1
이라고 점화식을 세울 수 있다.

그렇다면, 나머지 경우인 비교한 문자가 같지 않은 경우는 어떻게 점화식을 세울 수 있을까?
s1: a c
s2: capc a
인 경우,

c와 a는 비교했을 때 문자가 같지 않으므로, 각각 두 문자를 비교하기 전인

s1: ac
s2: capc
일 때의 lcs나

s1: a
s2: capca
일 때의 lcs 중에서 최대 lcs를 가지면 된다. 따라서 점화식은
lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

정리하면,
1. 비교한 문자가 같은 경우,
lcs[i][j] = lcs[i-1][j-1] + 1
2. 비교한 문자가 같지 않은 경우
lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

팁
2차원 배열에서 최댓값 추출하는 방법
map() 함수를 이용하기
max(map(max, arr))
=> arr 이차배열들의 각 원소 배열 중에서 가장 큰 값을 가진 요소로만 배열을 생성
그럼 그 배열 중에서 가장 큰값을 추출하는 함수이다.
"""

import sys  
input = sys.stdin.readline

s1 = list(input())
s2 = list(input())

lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(max(map(max, lcs)))
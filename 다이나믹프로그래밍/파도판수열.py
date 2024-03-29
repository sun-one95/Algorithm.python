'''
백준 9461

문제를 읽어보면 파도판 수열의 나선의 길이들이 아래와 같이
1, 1, 1, 2, 2, 3, 4, 5, 7, 9... 으로 이루어진다.

이 숫자들을 통해 규칙을 찾을 수 있다.

처음 3번째까지는 규칙이 없고 4번째부터 보면 피보나치 수열이라는 걸 찾을 수 있다.
하지만, 바로 전숫자와 전전숫자의 합이 아니라 i-2, i-3번째 숫자들의 합으로 i를 만들 수 있다.

그리하여 위의 규칙으로 p(n)에 대한 식을 짤 수 있다.
'''

p = [0 for i in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1

for i in range(4, 101):
    p[i] = p[i-2] + p[i-3]

for tc in range(int(input())):
    n = int(input())
    print(p[n])


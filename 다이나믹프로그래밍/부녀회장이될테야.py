'''
백준 2775

k, n = 1, 3
1층 3호 사람
0층 1호 = 1 + 0층 2호 = 2 + 0층 3호 = 3 = 6

d0 = [1, 2, 3] => [1, 3, 6]
for i in range(2):
    for j in range(1, 3):
        d0[1] += d0[0] = 3
        d0[2] += d0[1] = 6

        d0[1] += d0[0] = 4
        d0[2] += d0[1] = 10

주어진 입력값 k, n를 입력받고
각 호에 대한 인원수가 주어진게 0층 이므로 0층에 관한 호 인원들을 리스트로 만들어 저장한다.
그리고 층 수 k만큼 반복문을 돌려서 1부터 주어진 호 수 n까지 반복문 돌려서
원래 초기 0층에 관한 호 수 인원들의 값을 갱신한다.(이제는 0층에 관한 값이 아니라 1층 ... k - 1층에 관한 식으로 변함)
'''

for tc in range(int(input())):
    floor = int(input()) # 층
    num = int(input()) # 호
    d0 = [i for i in range(1, num + 1)] # 0층 리스트
    for i in range(floor): # 층 수 만큼 반복
        for j in range(1, num): # 1 ~ n - 1까지 (인덱스로 사용)
            d0[j] += d0[j-1] # 층별 각 호실의 사람 수를 변경

    print(d0[-1]) # 가장 마지막 수 출력




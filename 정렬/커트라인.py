'''
백준 25305

커트라인 k인 합격자들 가운데, 가장 낮은 점수의 합격자를 리턴하는 문제
즉, 시험에 응시한 학생들의 점수를 내림차순 정렬하고, 그 배열의 k - 1 번쨰 요소를 출력하면
합격한 점수의 최저점을 출력할 수 있다.
'''

n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort(reverse=True)
print(x[k - 1])

'''
백준 2822

첫째 줄에 참가자의 총점을 출력한다.(가장 높은 점수 5개의 합)
둘째 줄에는 어떤 문제가 최종점수에 포함되는 지를 공백으로 구분하여 출력한다. (문제 번호를 출력)

내가 푼 풀이
- 리스트를 두개 만들어줘서 하나는 그냥 정렬하지 않고 입력받은 순서대로 나열한 리스트고, 다른 하나는 내림차순으로 정렬을 실행하고
0에서 4까지만 자른 리스트이다.
- 그리하여 두번째 리스트를 sum() 내장함수를 통해서 최종점수를 구한다.
- 그리고 첫번째 리스트를 반복문돌려서 그 요소값이 두번째 리스트에 있다면, 그 인덱싱값을 1더해서 출력한다.
'''
arr = []
ans = []
for i in range(8):
    num = int(input())
    arr.append(num)
    ans.append(num)

ans.sort(reverse=True)
ans = ans[0:5]
result = sum(ans)
print(result)

for i in range(8):
    if arr[i] in ans:
        print(i + 1, end=' ')

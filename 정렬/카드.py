'''
백준 11652

파이썬 딕셔너리를 이용해서 문제를 풀었다.
일단 n개의 정수를 담을 리스트를 만들어서 정수를 담아준다.
그리고 딕셔너리를 선언해서 그 숫자들을 키로 잡고 개수를 값으로 잡는다.
그리고 새로운 리스트를 하나 선언, 딕셔너리의 최댓갑을 담을 변수를 선언해준다.
딕셔너리를 for 문을 돌려서 그 값과 동일한 key를 리스트에 담아준다.
리스트를 정렬해준 다음, 가장 첫번째 요소를 출력해주면 된다.
'''

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
dic = {}
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

list = []
num = max(dic.values())

result = 0
for i in dic:
    if num == dic[i]:
        list.append(i)

list.sort()
print(list[0])
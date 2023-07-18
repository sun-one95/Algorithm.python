'''
백준 2562

max 함수를 통해서 받아온 입력값들중에서 가장 큰 숫자를 찾고
index 함수를 통해서 그 최댓값이 몇번째에 위치하는지 찾아서 1더해준 값으로 리턴해준다.
'''

arr = []
for i in range(9):
    num = int(input())
    arr.append(num)

max_value = max(arr)

result = arr.index(max_value) + 1

print(max_value)
print(result)
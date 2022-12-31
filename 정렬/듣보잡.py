'''
백준 1764

듣도 못한 사람과 보도 못한 사람들 중에서 중복디는 인원을 찾아 사전순으로 나열하면 끝이다.
반복문을 통해서 곁치는 게 있는지 찾고 그 다음에 찾은 인원들을 사전순으로 오름차순 정렬시킨다.
'''

n, m = map(int, input().split())
arr_n = [] # 듣도 못한 사람
arr_m = [] # 보도 못한 사람

for i in range(n):
    arr_n.append(input())

for j in range(m):
    arr_m.append(input())

arr_n.sort()
arr_m.sort()
result = [] # 듣도 보도 못한 인원

def bs(arr, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return None

for i in range(m):
    target = arr_m[i]
    idx = bs(arr_n, target, 0, m - 1) 
    if idx != None:
        result.append(arr_n[idx])


print(len(result))
for i in result:
    print(i)





result.sort()
print(len(result))
for i in result:
    print(i)



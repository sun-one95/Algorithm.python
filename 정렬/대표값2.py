'''
백준 2587

주어진 정수 리스트들을 정렬하여 중간 위치의 인덱싱의 값을 리턴한다.
'''

arr = []
for i in range(5):
    n = int(input())
    arr.append(n)

arr.sort()

print(sum(arr) // 5)
print(arr[2])

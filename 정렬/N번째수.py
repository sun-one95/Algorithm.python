'''
백준 2693

10개의 숫자들을 입력받아서 내림차순 정렬을 한뒤에
인덱싱 2번째 요소값을 출력하면 된다.
'''

for tc in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    print(arr[2])


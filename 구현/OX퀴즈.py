'''
백준 8958

문자열을 리스트로 전환하고
변수 cnt를 0으로 초기 설정해서 반복문을 돌릴때마다 O가 나오면 1씩 cnt를 올려서 결과갑 변수 result 에 cnt를 더해준다.

O가 아니라면 cnt를 다시 0으로 초기설정한다.
'''

for tc in range(int(input())):
    str = input()
    arr = list(str)

    result = 0
    cnt = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    
    print(result)
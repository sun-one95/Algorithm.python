'''
백준 5052

내가 처음에 숫자를 입력받을 때, 넘버 타입으로 받고 그 다음에 리스트에는 문자열 타입으로 넣으려고 했는데,
그냥 애초에 입력값부터 문자열로 받아도 상관이 없었다.

그러면, 그 문자열들을 담은 리스트를 정렬시키면 결국에는 오름차순 정렬이기 때문에 비슷한 숫자들이 연달아서 나올것이다.
그렇기 때문에 이렇게 세팅을 하면 반은 온것이다.

마지막으로 for 문을 n - 1 번째 까지 돌려서
i번쨰 숫자와 i + 1[i번째 길이]의 숫자가 같다면 일관성이 없다는 뜻
따로 만들어준 불린값(flag=True)을 falase로 재할당하고 종료시키면 된다.
'''

for tc in range(int(input())):
    n = int(input()) # 번호의 개수
    nums = []
    for i in range(n):
        nums.append(input()) 
    nums.sort() # 받은 번호를 정렬
    flag = True # 일관성이 있는지 없는지 불린값을 선언
    for i in range(n-1):
        long = len(nums[i]) # 숫자의 길이
        if nums[i] == nums[i + 1][:long]: # 만약 i번째 숫자와 i + 1 번째의 i번째 숫자 길이만큼의 숫자가 같다면
            flag = False # 일관성이 없다.
            break
    if flag: # 일관성이 있으면
        print('YES')
    else: # 일관성이 없으면
        print('NO')
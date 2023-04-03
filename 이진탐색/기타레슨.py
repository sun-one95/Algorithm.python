'''
백준 2343

주어진 강의의 수(n)를 주어진 블루레이 개수(m)개에 담아야 한다.
각 블루레이에 강의를 담을 시 조합할 수 있는 블루레이의 최소 길이를 구해야 한다.

이러한 문제도 이진탐색으로 풀 수 있을 줄을 생각도 못했다.
start = 0, end = 1000000000(각 강의의 길이 < 10000분이고 주어진 강의의 수의 최댓값은 100,000이므로 대략 이들의 곱해서 나올 수 있는 길의의 최댓값이라 구한다.)
mid는 찾으려는 강의의 길이라고 설정하고 찾는다.
'
1. 만약 mid값이 현재 주어진 강의길이 리스트의 최댓값보다 작다면 애초에 시작을 못하기 때문에
mid값을 높여줘야 한다. 그러므로 start = mid + 1 로 재설정한다.

2. 블루레이 개수(cnt)와 블루레이 길이(tmp)를 갱신할 변수를 두개 설정한다.

3. n번 만큼 for 문을 돌려서 마약 tmp 에서 현재 강의 길이를 더한 값이 mid 보다 작거나 같다면
tmp += data[i] 로 갱신해준다.

4. 아니라면 블루레이의 강의가 꽉찼다는 의미이므로 cnt += 1해주고 다음 블루레이를 사용한다.
그리고 다음 블루레이에는 시작점이 0이아니라 아까 data[i] 값으로 초기화 시켜준다.

5. 반복문이 끝나고 블루레이 개수가 m개 이하라면, 일단 답의 후보이므로
결과로 제출할 변수(result) 를 초기화시켜준다(가장 작은 값으로 비교하며)
그리고 end = mid - 1 갱신하여 mid 값을 더 낮춰서 해본다.

6. 만약 cnt가 m 이상이라면 mid 값을 높여줘야 하므로 start = mid += 1 한다.

솔직히 아직도 이분탐색의 응용 문제는 나에게 어렵다.
하지만 문제를 풀다보면 유형에 익숙해지는 것 같다. 초기 생각만 빌드업 한다면 
잘 풀 수 있을 것 같다.
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))


#순서를 유지해야 하므로 정렬을 사용하면 안된다.
# 이분탐색을 두번 적용 시켜서 
num = sum(data)

start = 0 
end = 10000000000
result = num

while start<=end:
    # mid 는 블루레이 크기
    mid = (start+end) // 2 
    if mid < max(data):
        start = mid + 1
        continue
    # cnt 는 블루레이 개수 , tmp 는 블루레이 갱신해주고 있는 블루레이 길이
    cnt,tmp =1,0
    # 하나씩 더하면서 갱신해준다. 
    for i in range(n):
        # 이전 값이랑 지금 값 더해서 mid 보다 작으면 계속 더해준다
        if tmp + data[i] <= mid:
            tmp += data[i]
        # mid 보다 커지면 현재 data[i]가 tmp 로 들어가고
        # 전에 있던 tmp는 0 초기화 해주고 개수 1개 늘려준다.
        else:
            tmp = data[i]
            cnt += 1
    # 개수가 m보다 작거나 같으면 이분탐색으로 영상 길이 인 mid값 갱신 로직 실행ㄴ
    if cnt <= m:
        end = mid - 1
        result = min(result,mid)
    else:
        start = mid + 1
print(result)
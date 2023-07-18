'''
백준 11000

1. 먼저, 회의의 [시작, 끝] 시간을 새로 만든 리스트에 저장한다.
2. 시작시간을 기준으로 정렬을 한다. 그럼 시작시간이 빠른 순서대로 정렬된다.
3. 우선순위 큐를 이용해서 큐에 첫번쨰 요소의 끝 시간을 넣어준다.
4. 두번쨰 회의부터 비교를 하는데 첫째 회의의 끝시간보다 두번쨰 회의 시작시간이 크거나 같다면 회의실을 이어서 진행할 수 있다.
5. 그래서 코드를 room에서 한번 pop을 해줘서 첫째 회의 시간을 빼주고 아까 4에서 두번쨰 회의 끝시간을 넣어준다.
6. 만약 4의 조건에 해당 되지 않는다면 새로운 회의실을 개설해야 한다.
7. 코드는 기존에 room에 6의 조건에 해당하는 회의의 끝시간을 넣어준다.
8. 다끝나면 room에 요소의 개수를 출력하면 된다.
'''
from heapq import heappush, heappop
n = int(input())
q = []

for i in range(n):
    s, t = map(int, input().split())
    q.append((s, t))

q.sort()

room = []
heappush(room, q[0][1])

for i in range(1, n):
    if room[0] > q[i][0]: # 현재 끝나는 시간보다 다음 회의 시작시간이 빠른면
        heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heappush(room, q[i][1])

print(len(room))



    
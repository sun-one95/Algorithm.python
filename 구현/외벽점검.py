from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer

# dist = [1, 2, 3, 4]
# ans = list(permutations(dist, len(dist)))
# print(ans)

# 이 문제는 제한 조건이 weak, dist 리스트의 길이가 매우 작은 것을 알 수 있다.
# 주어지는 데이터의 개수가 적을 때는 모든 경우를 일일이 확인하는 완전탐색으로 접근하려고 한다.
# 문제에서 찾고자 하는 값은 '투입해야 하는 친구 수의 최솟값'이다. 이때 전체 친구의 수는 초대 8이다.
# 따라서 모든 친구를 무작위로 나열하는 모든 순열의 개수를 계산해보면 8P8 = 8! = 40,320으로 충분히 계산 가능한 경우의 수가 된다.
# 따라서 친구를 나열하는 모든 경우의 수를 각각 확인하여 친구를 최소 몇 명 배치하면 되는지 계산하면 문제를 해결할 수 있다.

# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# result = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if data[i] != data[j]:
#             result += 1

# print(result)


n, m = map(int, input().split())
data = list(map(int, input().split()))

arr = [0] * 11

for x in data:
    arr[x] += 1

result = 0
for i in range(1, m + 1):
    n -= arr[i]
    result += arr[i] * n


# 볼링공의 총 개수가 n개이고, 공의 무게는 1 부터 m가지의 번호로 이루어져 있다.
# 두 사람이 선택시에 같은 무게의 번호를 고를 수 없다. 즉, 중복 무게 볼링공 선택 금지
# 입력값으로 주어진 각 번호의 무게들을 따로 배열을 만들어서 무게들의 개수를 기록한다.
# 그런 다음, 그 i 무게 개수에서 n - i의 개수를 곱해서 개수를 result 변수에 더한다.
# 반복문을 통해서 위와 같은 과정을 진행한다. 하지만, 내가 여기에서 헷갈렸던건 앞에서 i 무게의 개수에 대한 경우의 수를 구했으면
# 다음 번째 무게에 대한 경우의 수를 구할 때는 n개에서 전에 사용되었던 i 무게개수를 차감한 상태로 진행한다. 그래야 중복되지 않는다.
# 위 문제를 접근했을 때, 그냥 이중 반복문을 통해 i번째와 i + 1 번째를 비교하여 다를때만 result 에 +1을 했었다.
# 내 풀이보다는 위의 풀이를 좀 더 기억해야 다음 어려운 문제를 풀때, 신선하게 문제에 접근할 수 있을 것 같다.

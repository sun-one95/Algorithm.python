# 문자열은 오름차순으로 정렬, 숫자는 다 더한 값을 문자열 다음으로 붙여서 출력한다.
# 일단 반복문을 통해서 숫자인 걸 찾은 다음에 그것을 다 더하고 그 값을 변수에 할당하여 저장한 다음
# 문자는 따로 리스트에 담아서 오름차순으로 정럴한 다음 변수에 저장
# 이 두개를 마지막에 합쳐서 리턴한다.
# 내 풀이 코드
"""
s = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0 # 숫자의 합을 저장할 변수
str = [] # 문자들을 저장할 리스트 후에 sum을 합쳐서 답으로 리턴
for i in range(len(s)):
    val = s[i] in alphabet  # 알파벳 문자열 안에 s[i]가 포함되는 지 확인
    if val: # 포함 된다면 문자열 리스트에 푸쉬
        str.append(s[i])
    else: # 아니라면 숫자이므로 더해준다.
        sum += int(s[i])

str.sort() # 문자열 오름차순 정렬
str.append(sum) # 마지막에 더한 값을 마지막 위치에 삽입

for i in str:
    print(i, end='') # 뛰어쓰기 없이 문자열로 리턴
"""
# 레퍼런스 코드
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha(): # 알파벳 확인 내장함수, 숫자는 isdigit
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += x
    
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(value)

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

"""
나와 달랐던 점: 일단 문자열을 확인하는 내장함수가 있는 지 몰랐다. 그래서 나는 위의 방식대로 한건데, 좋은 방법을 알았다.
그리고 숫자가 입력받지 않았을 때를 가정하지 않았다. 이점 유의해야 겠다.
그리고 마지막 출력 하기 위해서 리스트를 문자열로 변환하는 방법도 레퍼런스 방식을 처음 보는데 한줄로 표현이 되니까 잘 익혔다가 써먹어야 겠다.
"""


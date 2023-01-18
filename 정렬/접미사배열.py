'''
백준 11656

주어진 문자의 접미사를 다 뽑아서 새 리스트에 저장을한다. 그런다음, 그 리스트를 오름차순 정렬시키면 된다.
접미사를 추출하는 방법은 문자의 길이만큼 반복문을 돌려서 s[i:] 이런식으로 문자를 하나씩 잘라서 리스트에 추가한다.
'''

s = input()
arr = []
for i in range(len(s)):
    str = s[i:]
    arr.append(str)

arr.sort()
for i in arr:
    print(i)
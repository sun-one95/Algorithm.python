'''
백준 1302
'''

n = int(input())
dic = {}
for i in range(n):
    book = input()
    if book not in dic:
        dic[book] = 1
    else:
        dic[book] += 1

list = []

num = max(dic.values())

for i in dic:
    if num == dic[i]:
        list.append(i)

list.sort()
print(list[0])
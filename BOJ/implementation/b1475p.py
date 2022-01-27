from collections import Counter

roomNo = list(input())
no = []

for i in roomNo:
    temp = i.replace('6','9')
    no.append(temp)


count = Counter(no)


max_key = max(count.keys())


if max_key == '9':
    print(max(count.values()) // 2)
else:
    print(max(count.values()))


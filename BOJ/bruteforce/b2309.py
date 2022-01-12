import random

tall = []

for i in range(9):
    size = int(input())
    tall.append(size)

while 1:
    # 7개를 랜덤으로 뽑아서 items배열에 담고 items의 sum값을 구해라
    items = random.sample(tall,7)
    sumValue = sum(items)

    #items들의 sum값이 100일때 items들을 정렬해서 값을 추출한다.
    if(sumValue == 100):
        items.sort()
        for i in items:
            print(i)
        break
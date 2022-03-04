X = int(input())

stickList = [64]

while 1:
    sumResult = 0

    if(sum(stickList) == X):
        break
    if(sum(stickList) > X):
        # 오름차순 정렬
        stickList.sort()
        # 첫번째 있는것이 가장 짧은거니까 절반으로 나누고
        first = stickList.pop(0)
        sumResult = (first//2 + sum(stickList))
        if(sumResult >= X):
            stickList.append(first//2)
        else:
            stickList.append(first//2)
            stickList.append(first//2)

print(len(stickList))

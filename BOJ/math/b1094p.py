X = int(input())
cnt = 0

stickList = [64]

while 1:
    if(sum(stickList) > X):
        # 오름차순 정렬
        stickList.sort()
        stickList[0]=stickList[0]//2
        cnt+=1
        if(sum(stickList) >= X):
            # 첫번째꺼마저 버린다.
            stickList.pop(0)



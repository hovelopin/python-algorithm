# 18시 15분 ( 시작 ) => 18시 32분 ( 끝 )
def solution(nums):
    from itertools import combinations as cb

    cnt = 0
    sumList = []
    print(list(cb(nums,3)))
    for i,j,k in cb(nums,3):
        sumList.append(i+j+k)
    print(sumList)

    for i in sumList:
        start = 2
        result = 0
        while i > start :
            if i%start == 0:
                result += 1
                break
            else:
                start += 1

        if result == 0:
            cnt += 1

    return cnt


solution([1,2,3,4])
# 12시 22분 (시작) => 12시 30분 ( 끝 )

def solution(absolutes, signs):
    result = 0

    for i in range(len(signs)):
        if signs[i] == True:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    print(result)


solution([4,7,12] , [True,False,True])
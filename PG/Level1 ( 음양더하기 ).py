def solution(absolutes, signs):
    sumValue = 0

    # signs의 부호를 확인해주고 +면 absolutes에서 하나 뽑아서 + 하고 -면 -해주고..
    for i in range(len(signs)):
        # true값을 표현하기위해 1이라는 값을 사용했다!
        if(signs[i] == 1):
            sumValue += absolutes[i]
        else:
            sumValue -= absolutes[i]
    return sumValue

solution([4,7,12],['true','false','true'])
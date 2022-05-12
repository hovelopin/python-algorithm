# 19시 45분 시작 =>

def solution(N, stages):
    # result를 만들어서 몇번 스테이지에서 몇명이 탈락하는지에 대한 확률을 넣어놓고
    result = [0] * (len(stages)+1)
    cnt = len(stages)
    # newResult는 실패율을 구해서 담는 배열
    newResult = []

    failRate = []
    # stage를 전부 돌면서 해당하는 index의 값을 1씩 증가시킨다.
    for i in stages:
        result[i] += 1
    print(result)

    # result를 N까지만 짤라서 그 안에서 확률을 만들어 새로운 배열에 넣는다.
    for i in result[1:N+1]:
        newResult.append(i/cnt)
        cnt-=i
    print(newResult)

    # 확률이 높은 순서대로 index번호를 찾고 +1 해준다.
    for i in range(N):
        idx = newResult.index(max(newResult))+1
        failRate.append(idx)
        newResult[idx-1] = -1

    return print(failRate)

solution(5,[2])

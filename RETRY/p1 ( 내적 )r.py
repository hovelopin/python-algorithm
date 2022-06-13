# 18시 10분 (시작) => 18시 12분 (끝)
def solution(a, b):
    answer = 0
    for i,j in zip(a,b):
        answer += i*j
    return answer


solution([1,2,3,4] , [-3,-1,0,2])
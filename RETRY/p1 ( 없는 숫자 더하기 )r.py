# 12시 15분 (시작) => 12시 18분 (끝)

def solution(numbers):
    result = [0,1,2,3,4,5,6,7,8,9]
    answer = 0

    for i in result:
        if i not in numbers:
            answer += i
    return answer

solution([1,2,3,4,6,7,8,0])
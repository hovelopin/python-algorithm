def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    # progresses가 0이 아닐때까지 반복한다.
    while len(progresses) != 0:
        # 가장 중요한 조건!! => 작업 진도 + 날짜 * 스피드가 100을 넘으면 지우고 카운트를 올린다.
        # 아닐때는 카운트를 확인하고 날짜를 증가시킨다.
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1

    answer.append(count)
    print(answer)
    return answer

solution([93, 30, 55] , [1, 30, 5])
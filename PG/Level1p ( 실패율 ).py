def solution(N, stages):
    answer = []
    result = {}

    cnt = 1
    # stages의 총 길이!
    stages_len = len(stages)
    # stages를 낮은순서대로 정렬
    # stages.sort()
    # print(stages)

    for i in range(1,N+1):
        fail = stages.count(i) / stages_len
        answer.append(fail)
        stages_len-= stages.count(i)

    for i in range(1,N+1):
        result[i] = answer[i-1]

    result = sorted(result.items())

    print(answer)
    print(result)
    return answer


solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
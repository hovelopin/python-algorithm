# 정확성은 모두 맞았지만 시간초과나는 문제!

def solution(participant, completion):
    answer = ''

    for i in completion:
        if i in participant:
            participant.remove(i)


    answer = participant[0]
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
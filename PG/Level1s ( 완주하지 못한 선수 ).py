def solution(participant, completion):
    # n 제곱
    participant.sort()
    completion.sort()

    # print(participant)
    # print(completion)
    for p, c in zip(participant, completion):
        if p != c:
            return p
    print(participant)
    answer = participant.pop()
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
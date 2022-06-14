# 무조건 딕셔너리를 써야지 가능한 것 같음

def solution(participant, completion):
    from collections import Counter

    maraton = Counter(participant)

    for i in completion:
        maraton[i] -= 1

    for k,v in maraton.items():
        if v != 0:
            return k






solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
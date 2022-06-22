# 19시 15분 (시작) => 20시 12분 (끝) ==> 57분
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    counter = defaultdict(int)
    answer = []

    # 조합과 defaultdict를 사용해서 딕셔너리에 값을 한칸씩 증가시켜준다.
    for i in range(len(orders)):
        for j in course:
            # orders[i]번째 배열을 j개 만큼 튜플로 묶어준다.
            combi = list(combinations(orders[i],j))
            # 그리고 그것을 배열로 돌면서 해당하는부분에 값을 1씩 증가시켜준다.
            for k in combi:
                counter["".join(sorted(k))] += 1
    print(counter)
    # 그리고 value값을 기준으로 정렬해줘야한다.=> 정렬을 하면 딕셔너리에서 order 배열로 바뀜
    order = sorted(counter.items() , key = lambda x:-x[1])
    print(order)

    # 그리고 갯수를 카운트 해줄건데 내림차순으로 위에서 정렬해 준 이유는 maxValue가 마지막에 있을 경우를 생각했어야한다.
    for i in course:
        maxValue = 0
        temp = []
        for k,v in order:
            if len(k) == i and v >= 2 and maxValue <= v:
                temp.append(k)
                maxValue = v
        for j in temp:
            answer.append(j)

    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
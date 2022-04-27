from collections import defaultdict


def solution(id_list, report, k):
    # 결과값을 반환하기 위해 id_list만큼 배열을 만들고
    answer = [0] * len(id_list)

    # 주어지는 report 리스트를 중복 제거 해주는 것이 이 문제의 핵심이었다.
    # 이 한줄의 코드 없이 제출하면 수많은 시간초과를 만날 수 있다.
    report = set(report)
    # 유저 A가 신고한 유저 목록
    reportList = defaultdict(set)

    # 유저 A가 신고 당한 횟수
    reportedList = defaultdict(int)

    # k번 이상 신고당한 유저 목록을 담는다.
    suspended = []

    for r in report:
        #신고 한사람과 당한 사람을 split으로 바꾼다.
        report, reported = r.split()

        reportedList[reported] += 1
        reportList[report].add(reported)

        if reportedList[reported] == k:
            suspended.append(reported)

    for s in suspended:
        for i in range(len(id_list)):
            if s in reportList[id_list[i]]:
                answer[i] += 1

    return answer

solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)
# solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
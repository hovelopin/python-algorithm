def solution(id_list, report, k):
    dict = {}
    reportDict = {}
    reportList = []
    result = [0] * len(id_list)

    # 빈 배열을 넣어놓고
    for i in range(len(id_list)):
        dict[id_list[i]] = []
    # 신고받은 횟수를 딕셔너리에 넣기 위해서
    for i in range(len(id_list)):
        reportDict[id_list[i]] = 0

    # 누가 신고했는지에 대한 정보를 알기 위해서 report라는 배열을 split을 이용해 딕셔너리에 넣었다.
    for j in report:
        x,y = j.split()
        # value값에 데이터를 집어넣는것
        dict[x].append(y)
        reportDict[y] += 1
    print(dict)
    print(reportDict)

    for x,y in reportDict.items():
        if y >= k:
            reportList.append(x)
    print(reportList)



solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
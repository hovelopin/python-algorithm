# 10시 15분 => 45분까지

def solution(id_list, report, k):
    dic = dict()
    for i in report:
        start = i.split(' ')
        # start[0]은 신고자 start[1]은 신고 당한 사람
        # start[0]는 신고자 => dic에 key로 아직 없다면!
        if start[0] not in dic.keys():
            dic[start[0]] = [start[1]]
        else:
            # 신고 당한 사람이 신고한사람의 리스트에 없다면 추가해줘야지
            if (start[1] not in dic.get(start[0])):
                dic.get(start[0]).append(start[1])
    print(dic)
    cnt = [0]*len(id_list)

    for key in dic.keys():
        for j in dic[key]:
            if(key == )




solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
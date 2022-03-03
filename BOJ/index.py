from collections import Counter

# 10시 15분 => 45분까지

def solution(id_list, report, k):
    answer = []
    check_list = []

    dic = dict()

    for id in id_list:
        dic[id] = []

    for i in report:
        id , name = i.split()
        if name not in dic[id]:
            dic[id].append(name)
            check_list.append(name)

    
    print(dic)
    print(check_list)

    cnt = Counter(check_list)

    for id in id_list:
        answer.append(len([check for check in dic[id] if cnt[check] >= k]))
    print(answer)
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
# 19시 35분 (시작) => 20시 ( 끝 )

def solution(answers):
    # 1 2 3 4 5
    # 2 1 2 3 2 4 2 5
    # 3 3 1 1 2 2 4 4 5 5
    first , second , third = [1,2,3,4,5] , [2,1,2,3,2,4,2,5] , [3,3,1,1,2,2,4,4,5,5]
    cnt_1 , cnt_2 , cnt_3 = 0 , 0 , 0
    idx = 0
    answer = []

    for i in answers:
        if i == first[idx % 5]:
            cnt_1 += 1
        if i == second[idx % 8]:
            cnt_2 += 1
        if i == third[idx % 10]:
            cnt_3 += 1

        idx += 1

    if cnt_1 == max(cnt_1,cnt_2,cnt_3):
        answer.append(1)
    if cnt_2 == max(cnt_1,cnt_2,cnt_3):
        answer.append(2)
    if cnt_3 == max(cnt_1,cnt_2,cnt_3):
        answer.append(3)
    return answer

solution([1,3,2,4,2])
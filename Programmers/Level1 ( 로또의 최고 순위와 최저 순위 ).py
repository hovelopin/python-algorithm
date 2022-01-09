# 로또 번호를 담은 배열 lottos , 당첨번호를 담은 배열 win_nums

# answer  = 최고순위 , 최저순위를 담은 배열

# 정답은 맞았지만 if-else문을 난사..

def solution(lottos, win_nums):
    max_cnt = 0 ; min_cnt = 0
    max_grade = 0 ; min_grade = 0

    answer = []

    # 최저 순위를 뽑는 방법
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            # 당첨번호중에 하나를 기준으로 내가 고른 i가 당첨번호랑 같다면 값을 증가
            # 같으면 break를 통해서 다른 당첨번호랑 비교하고 아니면 다시 반복문을 돌아서 비교
            if(win_nums[j] == lottos[i]):
                min_cnt+=1
                break
    max_cnt = min_cnt + lottos.count(0)

    if(max_cnt == 6 ):
        max_grade = 1
    elif(max_cnt == 5 ):
        max_grade = 2
    elif(max_cnt == 4):
        max_grade = 3
    elif (max_cnt == 3):
        max_grade = 4
    elif (max_cnt == 2):
        max_grade = 5
    else:
        max_grade = 6

    # 최고순위값 answer에 삽입
    answer.append(max_grade)
    if (min_cnt == 6):
        min_grade = 1
    elif (min_cnt == 5):
        min_grade = 2
    elif (min_cnt == 4):
        min_grade = 3
    elif (min_cnt == 3):
        min_grade = 4
    elif (min_cnt == 2):
        min_grade = 5
    else:
        min_grade = 6
    answer.append(min_grade)

    return answer

solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])
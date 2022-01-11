# 효율성 5.4점 문제..
# 어떤 테스트 케이스에서 오류나는지 확인해봐야할듯

def solution(food_times, k):
    resultSum = 0

    if sum(food_times) <= k:
        return -1

    idx = 0  # 먹는 순서 위치
    cnt = 0

    while 1:
        # cnt == k 이면 break로 빠져나가
        if cnt == k:
            idx = idx % len(food_times)
            break
        # 인덱스 값을 설정해준다.
        idx = idx % len(food_times)

        # food_times[idx] 값이 0이면 인덱스값을 한칸 올리고 반복문 다시돈다
        if(food_times[idx] == 0):
            idx+=1
            continue
        # 만일 0이 아니면
        else:
            #idx값을 한칸 내린다!
            food_times[idx] -=1
        idx += 1
        cnt += 1

    return food_times[idx]


print(solution([3, 1, 2], 5))
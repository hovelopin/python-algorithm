def solution(answers):
    value = []

    cnt_1 = 0 ; cnt_2 = 0 ; cnt_3 = 0

    first = [1 , 2 , 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(1,len(answers)+1):
        remainder_1 = i % len(first)
        remainder_2 = i % len(second)
        remainder_3 = i % len(third)

        if(answers[i-1] == first[remainder_1-1]):
            cnt_1+=1
        if(answers[i-1] == second[remainder_2-1]):
            cnt_2+=1
        if(answers[i-1] == third[remainder_3-1]):
            cnt_3+=1

    if(cnt_1 == max(cnt_1,cnt_2,cnt_3)):
        value.append(1)
    if (cnt_2 == max(cnt_1, cnt_2, cnt_3)):
        value.append(2)
    if (cnt_3 == max(cnt_1, cnt_2, cnt_3)):
        value.append(3)

    return value

solution([1,3,2,4,2])
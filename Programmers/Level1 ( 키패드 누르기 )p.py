# 푸는중..
def solution(numbers, hand):
    answer = ''

    key_list = ['','00', '01', '02', '10', '11', '12','20','21','22','30','31','32']

    keypad = [
        [1,4,7,'*'],
        [2,5,8,0],
        [3,6,9,'#']
    ]

    store_left = ''
    stroe_right = ''

    answer_hand = ['R','L']

    for i in range(len(numbers)):
        if numbers[i] in keypad[0]:
            answer = answer +'L'
            store_left = key_list[numbers[i]]
        elif numbers[i] in keypad[2]:
            answer = answer + 'R'
            store_right = key_list[numbers[i]]
        else:
            compare(store_left, store_right, key_list[numbers[i]])
    print(answer)
    return answer


def compare(left, right , idx):




solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] , "right")

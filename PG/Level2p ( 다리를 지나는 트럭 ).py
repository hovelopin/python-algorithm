from collections import deque

deq = deque()

def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 다리의 크기를 알 배열
    stand = []

    while 1:
        for i in range(len(truck_weights)):
            stand.append(truck_weights)

            # deq 길이가 2를 넘지 않고 대기열에 넣은 weight가 기준 weight를 넘지 않는다면..
            if(len(deq) <= bridge_length and sum(stand) <= weight):
                deq.append(truck_weights)
                answer+=1
            else:
                if(len(deq) <= bridge_length):
                    deq.append(0)


    return answer

solution(2,10,[7,4,5,6])

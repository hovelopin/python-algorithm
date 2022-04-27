def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    phone = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']
    ]
    #시작하기전에 현재 왼손 오른손의 위치를 알아두고
    curLeftHand = '*'
    curRightHand = '#'

    for i in numbers:
        if i in left:
            answer += 'L'
            curLeftHand = i
        elif i in right:
            answer += 'R'
            curRightHand = i
        else:
            # 이제 여기서 조건을 걸어야 하는데 이동거리가 같을 경우에는 오른손 잡이 왼손잡이를 따져서 넣어야한다
            # =====> 생각
            # 왼손과 오른손의 현재 위치를 찾고 i를 찾아서 index끼리 절대값을 빼주면 그게 거리를 구할수있다.
            # 2중포문을 돌아서 찾으면 너무 시간초과가 날것같은 기분이 ,,
            for x in range(4):
                for y in range(3):
                    if(phone[x][y] == curLeftHand):
                        left_x = x
                        left_y = y
                    elif(phone[x][y] == curRightHand):
                        right_x = x
                        right_y = y
                    elif(phone[x][y] == i):
                        find_x = x
                        find_y = y

            left_dis = abs( left_x - find_x) + abs(left_y - find_y)
            right_dis = abs( right_x - find_x) + abs(right_y - find_y)

            if( left_dis == right_dis ):
                answer += hand[0].upper()
                if(hand[0].upper() == 'R'):
                    curRightHand = phone[right_x][right_y]
                else:
                    curLeftHand = phone[left_x][left_y]
            elif(left_dis < right_dis):
                answer += 'L'
                curLeftHand = phone[left_x][left_y]
            else:
                answer += 'R'
                curRightHand = phone[right_x][right_y]
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")
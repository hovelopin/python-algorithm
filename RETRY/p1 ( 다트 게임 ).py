"""
스타상 : 해당점수 *2 + 이전점수 * 2 , 처음에 나올시에는 그 점수만 * 2
아차상 : 해당점수 마이너스
"""

def solution(dartResult):
    temp_list = []
    temp = ""
    idx = -1

    for dart in dartResult:
        if dart == "S":
            temp_list.append(int(temp) ** 1)
            temp = ""
            idx += 1
        elif dart == "D":
            temp_list.append(int(temp) ** 2)
            temp = ""
            idx += 1
        elif dart == "T":
            temp_list.append(int(temp) ** 3)
            temp = ""
            idx += 1
        elif dart == "*":
            if idx < 1:
                temp_list[idx] = temp_list[idx] * 2
            else:
                temp_list[idx] = temp_list[idx] * 2
                temp_list[idx-1] = temp_list[idx-1] * 2
        elif dart == "#":
            temp_list[idx] = temp_list[idx] * -1
        else:
            temp += dart
    return print(sum(temp_list))

solution("1S2D*3T")
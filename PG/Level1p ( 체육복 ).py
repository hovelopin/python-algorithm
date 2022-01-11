# 테스트 케이스 모두를 통과 못한 문제!
# 정확성 55점..
# 여벌의 체육복을 가져온 학생이 체육복을 도난 당했을 경우를 찾지 못함!

def solution(n, lost, reserve):
    answer = 0
    # 전체 학생 수 에서 잃어버린 학생수를 빼면 나머지 학생들은 모두 체육수업을 들을 수 있음
    cnt = n -len(lost)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost in reserve:
                del reserve[lost]
                break
            if(lost[i] - 1 == reserve[j]):
                cnt+=1
                reserve.pop(0)
                break
            elif(lost[i] + 1 == reserve[j]):
                cnt+=1
                reserve.pop(0)
                break
    print(cnt)

    return answer

solution(5,[2,3,4],[1,3,5])
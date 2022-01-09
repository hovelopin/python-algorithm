# 테스트 케이스 모두를 통과 못한 문제!

def solution(n, lost, reserve):
    answer = 0
    # 전체 학생 수 에서 잃어버린 학생수를 빼면 나머지 학생들은 모두 체육수업을 들을 수 있음
    cnt = n -len(lost)

    for i in range(len(lost)):
        for j in range(len(reserve)):
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

solution(3,[3],[1])
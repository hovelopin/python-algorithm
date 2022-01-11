# 
def solution(nums):
    answer = 0

    #nums를 2로 나눈 다음 정수값만큼 가질수있다!
    pick = int(len(nums)/2)

    # 만일 중복을 제거하고 종류를 셀때 내가 가질 수 있는 종류보다 많을 경우에는 answer에는 pick값까지만 가질 수 있다.
    # else에 경우에는 answer에는 중복을 제거하고 남은 가짓수 정도만 가질 수 있다.
    if(len(set(nums)) > pick):
        answer = pick
    else:
        answer = len(set(nums))

    return answer

solution([3,3,3,2,2,2])
def solution(n, lost, reserve):
    cnt = 0

    # 1은 => 체육복 있음 , 0은 => 없음
    ans = [1] * (n+1)
    # 여분 체육복 가져온 사람들을 1씩 올려줌
    for i in reserve:
        ans[i] += 1
    # 잃어버린 사람들을 1을 빼준다.
    for i in lost:
        ans[i] -= 1

    # ans를 반복문으로 돌면서
    for idx in range(1, len(ans)):
        # ans가 0일때 검사를 시작해! 그리고 0인 놈의 앞뒤를 체크하는거야 걔내꺼에서 빌려와야되니까
        if ans[idx] == 0:
            # 2인 경우라는거는 여분을 가지고 있다는거니까 남에게 빌려줄수있자나 그래서
            if ans[idx-1] == 2:
                ans[idx-1] -= 1
                ans[idx] += 1
                continue
            # idx가 마지막 원소를 가리키지 않고
            if idx != len(ans) - 1:
                if ans[idx+1] == 2:
                    ans[idx+1] -= 1
                    ans[idx] += 1
                    continue

    for i in range(1, len(ans)):
        if ans[i] >= 1:
            cnt += 1

    return cnt


solution(5,[2,4],[1,3,5])

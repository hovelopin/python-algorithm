# 11시50분 (시작) ~ 12시 2분 (끝) => 12분
def solution(lottos, win_nums):
    cnt = 0
    zero = 0

    # win_nums 안에 있는 i가 lottos 안에 있다면 cnt +=1
    for i in lottos:
        if i == 0:
            zero +=1
        if i in win_nums:
            cnt+=1

    # 순위 체크하기
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    maxRank , minRank= rank[cnt+zero] , rank[cnt]

    result = [maxRank,minRank]
    print(result)

solution([44, 1, 0, 0, 31, 25] ,[31, 10, 45, 1, 6, 19] )
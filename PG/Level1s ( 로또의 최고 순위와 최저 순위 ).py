# 깔끔한 코드!

def solution(lottos, win_nums):
    # 6을 2개를 쓴 이유는 1개만 맞춰도 6등 다틀려도 6등
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    # 2중 for문을 돌리지 않고 if문을 통해 lottos안에 x가 있으면 값을 증가!!
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

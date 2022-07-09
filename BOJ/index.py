from itertools import combinations

n, m  = map(int,input().split())
check = [list(map(str,input().split())) for _ in range(m)]

numbers = [str(i) for i in range(10)]

number_combi = list(combinations(numbers , 3))

print(number_combi)
print(check)

# 숫자 , strike , ball => check배열을 돌면서 확인
for num,s,b in check:
    for i, j, k in number_combi:
        # 스트라이크와 볼을 나눈다.
        strike, ball = 0, 0
        # 첫번째가 0이면 고려하지 않아도 됨
        if i == '0':
            continue
        # 아니면 num과 i,j,k를 비교해가면서 strike , ball 갯수를 구한다.
        else:
            # num을 list로 만든다음에 하나씩 비교해서 strike를 구해주고

        # s랑 strike랑 같으면서 b랑 ball이랑 같으면 number_combi 배열에서 지운다.
        if s != strike and b != ball:
            number_combi.remove((i, j, k))
print(number_combi)












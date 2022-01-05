# 테스트케이스 수 ex ) 10
T = int(input())

cnt = 0
result = 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    value = 0
    case = int(input())

    # 1000개의 점수를 score 리스트에 담는다.
    score = sorted(list(input().split()))
    for i in score:
        result = score.count(i)
        if( cnt <= result ):
            maxValue = result
            value = i
            cnt = result
    print(f'#{case} {value}')
    cnt = 0
    result = 0
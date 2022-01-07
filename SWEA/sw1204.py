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
        # 첫번째 부터 검사해서 count를 통해서 몇개인지 검사한다.
        result = score.count(i)
        if( cnt <= result ):
            # 정렬했기 때문에 가장 뒤에 들어가는 value값이 같은 값중에서 큰 값이다.
            value = i
            cnt = result
    print(f'#{case} {value}')
    # 꼭 초기화를 해줘야함!
    cnt = 0
    result = 0
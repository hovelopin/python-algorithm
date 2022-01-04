# 내가 접근한 틀린 답! 정답이랑 비교해서 뭐가 다른지 확인하기

T = int(input())

cnt = 0
resultSum = 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    test = int(input())

    case = list(map(int,input().split()))

    for i in range(len(case)-1):
        # 만일 첫번째 케이스가 가장 큰 값이면 아무것도 사지 않는것이 베스트니까 0을 반환하고 종료
        if(case[0] == max(case)):
            print('안녕하세요')
            break
        # 만일 앞에 있는 숫자가 뒤에 보다 크면 앞에꺼를 사지 않는다.
        # 크지 않으면 cnt에 담을꺼 , 근데 그 자리가 맥스 값이면 거기서 판매!
        # 아니라면 cnt 값을 +1 해준다.
        if(case[i] > case[i+1]):
            continue
        else:
            cnt+=1
            for j in range(len(case)):
                if(case[i] == max(case)):
                    resultSum = case[i] * cnt
                    cnt = 0
        print(resultSum)

print(case)



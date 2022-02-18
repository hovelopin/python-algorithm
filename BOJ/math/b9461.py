# 정답은 맞았지만 조금은 비효율적인 코드를 작성한 것 같다.
# 입력 시간을 줄이기 위해서 sys를 사용했고
import sys

case = int(sys.stdin.readline())
# 1,2,3번째는 고정값으로 1을 설정해주었다.
value = [1,1,1]

# cnt를 사용한게 뭔가 비효율적으로 느껴진다.
# 사용한 이유는 이중포문 안에 값을 3번째 인덱스부터 돌리기 위해 사용했고 그 안에 resultValue값을 만들기위해 사용했다.
cnt = 3
for i in range(case):
    N = int(sys.stdin.readline())
    # 1,2,3 일때는 그냥 1을 출력하고 끝
    if(N==1 or N==2 or N==3):
        print(1)
    else:
        for j in range(cnt,N):
            # 여기서 규칙이 나오는데 규칙은 찾으려는 값은 그 값을 기준으로 앞으로 2번째 , 3번째를 합 한 것이다.
            resultValue = value[cnt-3]+value[cnt-2]
            value.append(resultValue)
            cnt+=1
        # N번째는 index로 따지면 그전이라서 N-1번째 출력
        print(value[N-1])

'''
대부분의 사람들은 그냥 만들어놓고 그 자리번째 숫자를 구했다. 
이게 비효율적이라고 잠깐 생각했는데 왜 그렇게 생각했지,, 내가 짠 코드보다 나은것같다. 
'''


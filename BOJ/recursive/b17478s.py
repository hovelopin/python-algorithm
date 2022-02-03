cnt = 0

def chatbot(num , count):
    underline = '__'*(2*count)
    # 재귀에는 무조건 조건문을 넣어서 함수를 종료시켜야한다.
    if num == count:
        print(underline + '"재귀함수가 뭔가요?"')
        print(underline + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(underline + "라고 답변하였지.")
        return 0

    print(f'{underline}"재귀함수가 뭔가요?"')
    print(f'{underline}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f'{underline}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(f'{underline}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

    count+=1


    chatbot(num , count)
    # 조건을 만족하면 역으로 다시 호출해서 끝낸다! => 실행한 함수들을 다 종료하면서 값을 추출한다.
    print(f'{underline}라고 답변하였지.')

num = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
# 매개변수를 2개 놔야하는것만 알았으면 어렵지 않은 문제!
chatbot(num,cnt)
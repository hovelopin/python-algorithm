'''
파이썬에 잘 정리되어있는 라이브러리를 이용해서 살짝 애매하게 해결한 문제 .. 깔끔하지 못했다.
'''
# combination을 이용하기 위해 itertools를 이용
from itertools import *

T = []
while 1:
    # 여러개를 입력받을때는 리스트로 받아서 다른 리스트에 넣어준다.
    case = list(map(int,input().split()))
    # 첫번째가 0이면 반복문을 탈출하고 아니면 T라는 리스트에 넣는다.
    if case[0] == 0:
        break
    else:
        T.append(case)

# 첫번째는 갯수고 2번째부터 마지막까지 중에서 순서에 상관없이 6개를 뽑는다.
for i in range(len(T)):
    # printList안에는 combinations의 결과값이 튜플형태로 배열안에 넣어진다.
    printList = list(combinations(T[i][1:],6))
    # 그걸 하나씩 접근하기 위해서 이중포문을 사용해서 하나하나 접근하였다.
    for j in range(len(printList)):
        for k in range(len(printList[j])):
            print(printList[j][k] , end =' ')
        print()
    print()

'''
초반에 입력받는게 헷갈렸고 combinations로 입력받은 값들을 한칸씩 띄어서 출력하는방법에서 헷갈림
'''
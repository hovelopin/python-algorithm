T = []
while 1:
    # 여러개를 입력받을때는 리스트로 받아서 다른 리스트에 넣어준다.
    case = list(map(int,input().split()))
    if case[0] == 0:
        break
    else:
        T.append(case)
print(T)

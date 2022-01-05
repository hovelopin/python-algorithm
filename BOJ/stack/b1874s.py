cnt = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt+=1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if (stack[-1] == num):
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)

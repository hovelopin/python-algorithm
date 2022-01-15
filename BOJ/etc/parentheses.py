command = list(input())

stack = []
cnt = 0

for i in range(len(command)):
    # command라는 곳을 통해서 입력하면 input값이 하나하나씩 접근할수있게 됨 그래서 여는 괄호면 stack에 넣어
    # 그리고 cnt값을 늘려
    if(command[i] == '(' or command[i] == '[' or command[i] == '{'):
        stack.append(command[i])
        cnt+=1
    else:
        # 닫는 괄호가 들어오면 cnt 값을 줄이고 command라는 곳에 닫는 괄호와 너가 stack에 넣는 여는 괄호가
        # 짝이 맞아야 stack에서 제거해 아니면 제거 못하고 바로 break로 빠져나와 false값을 출력
        cnt -= 1
        # 만일 cnt가 음수면 처음부터 닫는 괄호가 나왔거나 닫는 괄호가 여는 괄호보다 많다는 뜻이야
        if (cnt < 0):
            break
        if(command[i] == ')' and stack[cnt] == '('):
            stack.pop()
        elif(command[i] == ']' and stack[cnt] == '['):
            stack.pop()
        elif(command[i] == '}' and stack[cnt] == '{'):
            stack.pop()
        else:
            break

if(len(stack) == 0 and cnt == 0):
    print('true')
else:
    print('false')



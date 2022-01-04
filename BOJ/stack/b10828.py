import sys

stack = []

# 스택에 x를 넣는 연산
def push(n):
    stack.append(n)

def pop():
    # stack에서 가장 정수를 빼고 그 수를 출력
    if(len(stack) > 0):
        print(stack[-1])
        stack.pop()
    # 만약 스택에 들어있는 정수가 없는 경우에는 -1 출력
    else:
        print(-1)

def size():
    return print(len(stack))

def empty():
    if(len(stack)>0):
        print(0)
    else:
        print(1)

def top():
    if(len(stack) > 0):
        return print(stack[-1])
    else:
        return print(-1)


for i in range(int(sys.stdin.readline())):
    order = list(sys.stdin.readline().split())
    if(order[0] == 'top'):
        top()
        continue
    elif(order[0] == 'size'):
        size()
        continue
    elif(order[0] == 'empty'):
        empty()
        continue
    elif(order[0] == 'pop'):
        pop()
        continue
    else:
        push(order[1])
        continue



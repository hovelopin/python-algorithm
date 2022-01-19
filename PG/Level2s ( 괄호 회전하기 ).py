from collections import deque

def solution(ip):
    def check(s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                # stack이 비어있으면! return false 비어있다는 말은 닫는괄호부터 들어왔다는 뜻
                # 파이썬에서 empty list는 false , empty가 아닌 list는 true를 리턴
                if not stack:
                    return False
                x = stack.pop()
                if c == ')' and x != '(':
                    return False
                elif c == ')' and x != '(':
                    return False
                elif c == '}' and x != '{':
                    return False
        return len(stack) == 0

    ip = deque(ip)
    answer = 0

    for x in range(len(ip)):
        # deque를 왼쪽으로 한칸씩 민다.
        ip.rotate(-1)
        if check(ip):
            answer += 1
    return answer
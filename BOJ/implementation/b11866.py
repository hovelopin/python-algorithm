from collections import deque

n , k = map(int,input().split())

# 1부터 n까지의 숫자 circle을 만든다.
circle = deque([i for i in range(1,n+1)])
answer = []

print("<" , end="")
while circle:
    for i in range(k - 1):
        circle.append(circle.popleft())
    print(circle.popleft(), end = "")
    if circle:
        print(',' , end=" ")
print(">")

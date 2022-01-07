from collections import deque
import sys

deq = deque()

N = int(sys.stdin.readline())

# 1부터 N까지 deq에 담고
for i in range(1,N+1):
    deq.append(i)

# 마지막 한장이 남을때까지 반복한다.
while (len(deq) > 1):
    # 가장 왼쪽꺼 버리고
    deq.popleft()
    # 첫번째꺼를 맨뒤에 삽입하고
    deq.append(deq[0])
    # 첫번째꺼 버림
    deq.popleft()

print(deq[0])



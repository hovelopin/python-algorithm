from collections import deque

N , K = map(int,input().split())

deq = deque(range(1,N+1))

print('<', end='')

while deq:
    for i in range( K-1 ):
        deq.append(deq[0])
        deq.popleft()
    print(deq.popleft(), end='')
    if deq:
        print(',' , end ='' )
print('>')




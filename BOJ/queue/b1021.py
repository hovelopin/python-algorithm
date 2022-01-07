# 마지막 테스트 케이스만 틀림
# 2,3번을 최소로 하는 값을 구하는건데 중앙값일때 왼쪽으로 이동하는게 빠른건지 오른쪽으로 이동하는게 빠른건지 고민해야 함
# => 해결 절반으로 나눌때 index값 계산을 잘못함

from collections import deque

# 2,3번의 최솟값을 구하기

deq = deque()

N , M = map(int,input().split())

minValue = 0
cnt = 0

# deq안에 1~N값을 넣는다.
for i in range(1,N+1):
    deq.append(i)

# M개를 입력받아서 리스트에 넣고
command = list(map(int,input().split()))


for j in range(len(command)):
    for k in range(len(deq)):
        if(command[j] == deq[0]):
            deq.popleft()
            break
        else:
            # deq에 인덱스가 절반보다 크면 뒤에서부터 찾는다.
            if(deq.index(command[j]) > int(len(deq) / 2) ):
                #뒤에꺼를 빼서 앞으로 옮긴다.
                last = deq.pop()
                deq.appendleft(last)
                cnt+=1
            else:
                first = deq.popleft()
                deq.append(first)
                cnt+=1
print(cnt)





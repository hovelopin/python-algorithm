# 22시 50분 시작 => 23시 7분 끝

from collections import deque

computer = int(input())
number = int(input())

graph = [[] for _ in range(computer+1)]

for i in range(number):
    x , y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# 1번에 연결되는 컴퓨터의 수 출력
cnt = 0
# 0번노드 ~ computer노드 까지
visited = [0] * (computer+1)

def bfs(num):
    global cnt
    queue = deque()
    queue.append(num)
    visited[num] = 1

    while queue:
        # 값을 뽑아낸다.
        num = queue.popleft()
        for i in graph[num]:
            if( visited[i] == 0 ):
                queue.append(i)
                visited[i] = 1
                cnt+=1
    return cnt

print(bfs(1))
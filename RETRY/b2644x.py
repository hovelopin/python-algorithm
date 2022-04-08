from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    cnt = 0

    # queue가 빌떄까지 반복하는데
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            k = queue.popleft()
            # 방문하려는게 찾으려는 n2랑 같으면 끝낸다.
            if k == n2:
                return cnt - 1
            for i in graph[k]:
                if visited[i] == 0:
                    visited[i] = 1
                    queue.append(i)
    return -1

# 촌수 계산
n = int(input())
n1 , n2 = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

visited = [0] * (n+1)

for i in range(m):
    x , y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(n1))

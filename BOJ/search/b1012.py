from collections import deque

t = int(input())

# 상하좌우로 탐색
dx = [-1, 1 , 0, 0]
dy = [0 , 0 ,-1 ,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append([nx,ny])
                graph[nx][ny] = 0

for i in range(t):
    m, n, k = map(int, input().split())
    cnt = 0
    graph = [[0] * m for _ in range(n)]

    # x가 가로 y가 세로
    for j in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1

    # m이 가로 n이 세로
    for k in range(n):
        for l in range(m):
            if graph[k][l] == 1:
                bfs(k,l)
                cnt += 1
    print(cnt)
